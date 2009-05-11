#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
import re
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

_DEBUG = True

class BaseRequestHandler(webapp.RequestHandler):
  
  def generate(self, template_name, template_values={}):
    values = {}
    values.update(template_values)
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, 'templates', template_name)
    self.response.out.write(template.render(path, values, debug=_DEBUG))

class MainPage(BaseRequestHandler):
    def get(self):
      self.generate('index.html')




def main():

  application = webapp.WSGIApplication([
    ('/', MainPage)
  ], debug=True)

  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
