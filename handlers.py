from __future__ import absolute_import

from google.appengine.api import users
from google.appengine.ext.webapp.util import login_required

from shortcuts import MyRequestHandler
from models import Burndown

class MainPage(MyRequestHandler):

    @login_required
    def get(self):
        user = users.get_current_user()
        c = {}
        c['burndowns'] = Burndown.gql('where owner = :1', user)

        self.render_to_response('burn/index.html', c)

urls = [('/', MainPage),
        ]