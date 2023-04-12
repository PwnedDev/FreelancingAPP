#!/usr/bin/env python3

# from __future__ import absolute_import
import elara

# Repeated database lookups have been avoided
class PostsDB:
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

    def apply_job(self, title, author):
        apply_bool = input("Do you want to apply? Y/N ")
        if apply_bool == "Y":
            app_desc = input("Write in detail about your proposal: ")
            app_budget = input("What is the price you are willing to do this project for? : ")
            app_time = input("What is the timeframe you can complete this project in? : ")
            app_index = self.curindex
            self.db.lpush('applications', title)
            self.db.lpush('appdesc', app_desc)
            self.db.lpush('appauth', author)
            self.db.lpush('appbudget', app_budget)
            self.db.lpush('apptime', app_time)
            self.db.lpush('appindex', app_index)
            self.db.commit()

    def browse_post(self):
        for i, title in enumerate(self.post_title):
            print("[{}] {}\n".format(i+1, title))
        zoom = int(input("Enter [index] for more info about it: ")) - 1
        if zoom in range(len(self.post_title)):
            self.curindex = zoom
            print(self.post_title[self.curindex])
            print(self.post_text[self.curindex])
            print(self.post_author[self.curindex])
            print(self.post_budget[self.curindex])
            print(self.post_time[self.curindex])
            print("\n")
        else:
            # Error handling has been added 
            print("Invalid index. Quitting...")
            return

    def create_post(self, title, text, author, time, budget):
        self.db.lpush('posttitle', title)
        self.db.lpush('posttext', text)
        self.db.lpush('postauthor', author)
        self.db.lpush('postbudget', budget)
        self.db.lpush('posttime', time)
        self.db.commit()
