# menu principal

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
import webapp2
from webapp2_extras import jinja2
from classes import save

class welcome_handler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()

        lang = save.current_lang()
        greeting_field = {"es": "Bienvenido a PollenPunk", "en": "Welcome to PollenPunk"}
        new_game_field = {"es": "Empezar de nuevo", "en": "New game"}
        load_game_field = {"es": "Continuar", "en": "Continue"}
        change_lang_field = {"es": "Cambiar idioma", "en": "Change language"}
        current_lang_field = {"es": "Idioma actual", "en": "Current language"}
        logout_field = {"es": "Cerrar sesion", "en": "Logout"}
        text_field = {"es": "Un juego 'escoge-tu-propia-aventura' creado con Google AppEngine.", "en": "A text-adventure game created with Google AppEngine."}

        template_values = {
            "greeting": greeting_field[lang],
            "user_name": user.nickname(),
            "new_game_text": new_game_field[lang],
            "load_game_text": load_game_field[lang],
            "logout_url": users.create_logout_url('/'),
            "lang": lang,
            "current_lang": current_lang_field[lang],
            "change_lang": change_lang_field[lang],
            "logout": logout_field[lang],
            "menu_text": text_field[lang]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("welcome.html", **template_values))


class change_lang_handler(welcome_handler):
    def post(self):
        save.change_lang()
        super(change_lang_handler, self).post()