#!/usr/bin/env python3
import elara

class postsdb(object):
  def __init__(self):
    self.db = elara.exe_secure(path="db/posts.db",  key_path="db/posts.key")
    self.applications = self.db.lnew('applications')
    self.app_index = self.db.lnew('appindex')
    self.app_desc = self.db.lnew('appdescr')
    self.app_author = self.db.lnew('appauth')
    self.app_budget = self.db.lnew('appbudget')
    self.app_time = self.db.lnew('apptime')
    self.curindex = 0 
  
  def apply_job(self, title, author):
    apply_bool = input("Do you want to apply? Y/N")
    if(apply_bool=="Y"):
      applications_array = self.db.get('applications')
      apdesc_array = self.db.get('appdesc')
      apauth_array = self.db.get('appauth')
      apbudget_array = self.db.get('appbudget')
      aptime_array = self.db.get('apptime')
      apindex_array = self.db.get('appindex')
      app_desc = input("Write in detail about your proposal. : ")
      app_author = author
      app_budget = input("What is the price you are willing to do this project for? : ")
      app_time = input("What is the timeframe you can complete this project in? : ")
      app_index = self.curindex
      return self.db.lpush('applications', title), self.db.lpush('appdesc', app_desc), self.db.lpush('appauth', app_author), self.db.lpush('appbudget', app_budget), self.db.lpush('apptime', app_time), self.db.lpush('appindex', app_index), self.db.commit()
  def browse_post(self):
    posts_array = self.db.get('posttitle')
    desc_array = self.db.get('posttext')
    author_array = self.db.get('postauthor')
    budget_array = self.db.get('postbudget')
    time_array = self.db.get('posttime')
    for i in range(0, len(posts_array)):
      print("[{}] {}\n".format(i+1, posts_array[i]))
    zoom = int(input("Enter [index] for more info about it: "))
    zoom = int(zoom-1)
    if(zoom!="-1"):
      self.curindex = zoom
      print(posts_array[self.curindex])
      print(desc_array[self.curindex])
      print(author_array[self.curindex])
      print(budget_array[self.curindex])
      print(time_array[self.curindex])
      print("\n")
    else:
      print("Quitting...")
      return 0


  def create_post(self, title, text, author, time, budget):
    return self.db.lpush ('posttitle', title), self.db.lpush('posttext', text), self.db.lpush('postauthor', author), self.db.lpush('postbudget', budget), self.db.lpush('posttime', time), self.db.commit()

