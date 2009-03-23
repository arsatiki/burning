from __future__ import absolute_import

import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import urls

logging.getLogger().setLevel(logging.DEBUG)

application = webapp.WSGIApplication(urls, debug=True)
run_wsgi_app(application)