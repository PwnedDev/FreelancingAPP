#!/usr/bin/env python3
import elara

class logindb(object):
  def __init__(self, usr, pwd):
    self.username = usr
    self.password = pwd
    self.db = elara.exe_secure(path="db/accounts.db",  key_path="db/accounts.key") 
  
  def lgdb(self):
    if(self.db.lexists('username', self.username) and self.db.lexists('password', self.password) and self.db.get('username').index(self.username)==self.db.get('password').index(self.password)):
      return 0
    else:
      return 1 
   
