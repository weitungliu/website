#!/usr/bin/env python

"""main.py: Handler file to instantiate html templates with jinja."""

__author__ = "Kevin Frew"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Kevin Frew"
__email__ = "kevin@kevinfrew.com"

import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    autoescape=True)

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/main.html')
    self.response.write(template.render({}))

class AboutPage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    self.response.write(template.render({}))

class PhotoPage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/photography.html')
    self.response.write(template.render({}))

class ResumePage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/resume.html')
    self.response.write(template.render({}))

class ContactPage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
    self.response.write(template.render({}))

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/about/*', MainPage),
                               ('/photography/*', PhotoPage),
                               ('/resume/*', ResumePage),
                               ('/contact/*', ContactPage)])
