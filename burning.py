from __future__ import absolute_import

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import urls

application = webapp.WSGIApplication(urls, debug=True)