#!/usr/bin/env python3
import elara

class postsdb(object):
  def __init__(self):
    self.db = elara.exe_secure(path="db/posts.db",  key_path="db/posts.key")
    self.curindex = 0 
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
    if(zoom!="Q"):
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

