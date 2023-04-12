#!/usr/bin/env python3

import cherrypy
import elara

class PostsApp(object):
    def __init__(self):
        self.db = elara.exe_secure(path="db/posts.db", key_path="db/posts.key")
        self.applications = self.db.lnew('applications')
        self.app_index = self.db.lnew('appindex')
        self.app_desc = self.db.lnew('appdescr')
        self.app_author = self.db.lnew('appauth')
        self.app_budget = self.db.lnew('appbudget')
        self.app_time = self.db.lnew('apptime')
        self.post_title = self.db.get('posttitle')
        self.post_text = self.db.get('posttext')
        self.post_author = self.db.get('postauthor')
        self.post_budget = self.db.get('postbudget')
        self.post_time = self.db.get('posttime')
        self.curindex = 0 

    def apply_job(self, title, author, app_desc, app_budget, app_time):
        app_index = self.curindex
        self.db.lpush('applications', title)
        self.db.lpush('appdesc', app_desc)
        self.db.lpush('appauth', author)
        self.db.lpush('appbudget', app_budget)
        self.db.lpush('apptime', app_time)
        self.db.lpush('appindex', app_index)
        self.db.commit()

    def browse_post(self):
        posts = []
        for i, title in enumerate(self.post_title):
            posts.append("[{}] {}\n".format(i+1, title))
        return posts

    def get_post_details(self, index):
        if index in range(len(self.post_title)):
            self.curindex = index
            post_details = []
            post_details.append(self.post_title[self.curindex])
            post_details.append(self.post_text[self.curindex])
            post_details.append(self.post_author[self.curindex])
            post_details.append(self.post_budget[self.curindex])
            post_details.append(self.post_time[self.curindex])
            return post_details
        else:
            return None

    def create_post(self, title, text, author, time, budget):
        self.db.lpush('posttitle', title)
        self.db.lpush('posttext', text)
        self.db.lpush('postauthor', author)
        self.db.lpush('postbudget', budget)
        self.db.lpush('posttime', time)
        self.db.commit()

class PostsPage(object):
    def __init__(self, posts_app):
        self.posts_app = posts_app

    @cherrypy.expose
    def index(self):
        posts = self.posts_app.browse_post()
        post_list = ''
        for post in posts:
            post_list += post + '<br>'
        return """
            <html>
            <body>
            <h2>Available Jobs</h2>
            {}
            <form method="get" action="apply">
                <label>Job Index:</label>
                <input type="text" name="index">
                <label>Your Name:</label>
                <input type="text" name="name">
                <label>Your Proposal:</label>
                <textarea name="proposal"></textarea>
                <label>Price:</label>
                <input type="text" name="price">
                <label>Timeframe:</label>
                <input type="text" name="timeframe">
                <button type="submit">Apply
                """

class PostsPage:

    def __init__(self, posts_db):
        self.posts_db = posts_db

    @cherrypy.expose
    def index(self):
        return '''
            <html>
            <body>
            <form method="post" action="create_post">
            <label for="title">Title:</label>
            <input type="text" name="title" required><br>
            <label for="text">Text:</label>
            <textarea name="text" required></textarea><br>
            <label for="author">Author:</label>
            <input type="text" name="author" required><br>
            <label for="budget">Budget:</label>
            <input type="number" name="budget" required><br>
            <label for="time">Time:</label>
            <input type="text" name="time" required><br>
            <input type="submit" value="Create Post">
            </form>
            <br>
            <a href="/browse_posts">Browse Posts</a>
            </body>
            </html>
        '''

    @cherrypy.expose
    def create_post(self, title, text, author, budget, time):
        self.posts_db.create_post(title, text, author, time, budget)
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def browse_posts(self):
        # Display a list of posts and a form to apply for a job
        html = '<html><body>'
        for i, title in enumerate(self.posts_db.post_title):
            html += '<p>[{}]</p>'.format(i+1)
            html += '<p>Title: {}</p>'.format(title)
            html += '<p>Author: {}</p>'.format(self.posts_db.post_author[i])
            html += '<p>Budget: {}</p>'.format(self.posts_db.post_budget[i])
            html += '<p>Time: {}</p>'.format(self.posts_db.post_time[i])
            html += '<form method="post" action="apply_job">'
            html += '<input type="hidden" name="title" value="{}">'.format(title)
            html += '<input type="hidden" name="author" value="{}">'.format(self.posts_db.post_author[i])
            html += '<input type="submit" value="Apply">'
            html += '</form>'
            html += '<br>'
        html += '</body></html>'
        return html

    @cherrypy.expose
    def apply_job(self, title, author):
        # Form to apply for a job
        return '''
            <html>
            <body>
            <form method="post" action="submit_application">
            <input type="hidden" name="title" value="{}">
            <input type="hidden" name="author" value="{}">
            <label for="description">Description:</label>
            <textarea name="description" required></textarea><br>
            <label for="budget">Budget:</label>
            <input type="number" name="budget" required><br>
            <label for="time">Time:</label>
            <input type="text" name="time" required><br>
            <input type="submit" value="Submit Application">
            </form>
            <br>
            <a href="/browse_posts">Back to Posts</a>
            </body>
            </html>
        '''
        
if __name__ == "__main__":
    # Do something
