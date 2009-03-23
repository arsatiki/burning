from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template

class MyRequestHandler(webapp.RequestHandler):
    def render_to_response(self, template_name, context={}):
        content = template.render(template_name, context)
        self.response.out.write(content)
