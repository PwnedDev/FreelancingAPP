#!/usr/bin/env python3
import elara
class signupdb(object):
  def __init__(self, user, pwd):
    self.username = user
    self.password = pwd
    self.db = elara.exe_secure(path="db/accounts.db",  key_path="db/accounts.key")
  def accdb(self):
    return self.db.lpush('username', self.username), self.db.lpush('password', self.password), self.db.commit()
 
  def testprint(self):
    return self.db.get('username'), self.db.get('password')
    
