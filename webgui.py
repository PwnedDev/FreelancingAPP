#!/usr/bin/env python3
import cherrypy

class FreelancingGUI(object):
  def __init__(self):
    pass
  
  @cherrypy.expose
  def index(self):
    return """
    <html>
    <head>
    </head>
    <body>
      <form method="get" action="signup_send">
        <button type="submit"> Sign Up </button>
      </form>
      <form method="get" action="login_send">
        <button type="submit"> Login </button>
      </form> 
    </body> 
    </html>
    """

  @cherrypy.expose
  def login_send(self):
    return "Hello world"
  
  @cherrypy.expose
  def signup_send(self):
    return "Hello signup"
if __name__ == '__main__':
  cherrypy.quickstart(FreelancingGUI())

