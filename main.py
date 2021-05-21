# script principal

import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from webapp2_extras import jinja2

from handlers.login_handler import login_handler
from handlers.welcome_handler import welcome_handler
from handlers.welcome_handler import change_lang_handler
from handlers.zone_handler import zone_handler
from handlers.new_game_handler import new_game_handler
from handlers.load_game_handler import load_game_handler

app = webapp2.WSGIApplication([
    ('/', login_handler),
    ('/main_zone', welcome_handler),
    ('/change_lang',change_lang_handler),
    ('/new_zone', zone_handler),
    ('/new_game', new_game_handler),
    ('/load_game', load_game_handler)
    ],debug=True)