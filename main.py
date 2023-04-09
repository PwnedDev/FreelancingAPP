#!/usr/bin/env python3
from signup import signupdb
from login import logindb
from posts import postsdb
import time
class FreelancingAPP():
  def __init__(self):
    self.loginstate = False
    self.user = ""
  def startup(self):
    login_signup = input("Login/Register? L/R ")
    if(login_signup=="L"):
      self.user = input("Username: ")
      password = input("Passowrd: ")
      logon = logindb(self.user, password)
      if(logon.lgdb()==0):
        print("Logged in!")
        self.loginstate = True 
        return self.loginstate
      else:
        print("Invalid Credentials!")
    elif(login_signup=="R"):
      self.user = input("Username: ")
      password = input("Passowrd: ")
      signon = signupdb(self.user, password)
      print(signon.accdb()) 
    else:
      print("Invalid Query")
  def index(self):
    while(self.loginstate):
      browse_post = input("Browse or Post? B/P ")
      if(browse_post=="B"):
        bp = postsdb()
        bp.browse_post()
            
      elif(browse_post=="P"):
        bp = postsdb()
        title = input("Enter Title : ")
        author = self.user
        text = input("Enter description: ")
        budget = input("Enter budget ($): ")
        time = input("Enter timeframe : ")   
        print(bp.create_post(title, text, author, time, budget))
      else:
        print("Invalid Query")
    
    
  
    
     

if __name__ == '__main__':
  app = FreelancingAPP()
  app.startup()
  app.index()
