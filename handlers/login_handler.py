# handler para gestionar login de usaurios

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
import webapp2
from webapp2_extras import jinja2

from classes.save import load_user

class login_handler(webapp2.RequestHandler):
    def get(self):
        current_user = users.get_current_user()

        if current_user:
            # load user
            user = load_user()
            template_values = {"user_name": current_user.nickname()}
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("redirect.html", **template_values))
        else:
            # login
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.out.write(str.format("<a href=\"{0}\">Sign in or register</a>.",
                                               users.create_login_url('/')))
