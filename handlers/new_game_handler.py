# handler para comenzar una nueva partida

from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import ndb
from google.appengine.ext import db
import webapp2
from webapp2_extras import jinja2

from classes.save import *
from classes.zone import zone
from handlers.zone_handler import zone_handler

class new_game_handler(webapp2.RequestHandler):
    def post(self):
        # cargar primera zona
        current_zone_id = "intro"

        from classes.zone_manager import zones
        lang = current_lang()

        # crear o sobreescribir usuario
        user = load_user()
        user.zone = "intro"
        user.pollen = 20
        save_user(user)
        main_menu_fields = {"es": "Menu principal", "en": "Main menu"}
        pollen_fields = {"es": "Polen hostil en cavidad nasal", "en": "Hostile pollen in nasal cavity"}

        # crear pagina
        current_zone = zone(zones[current_zone_id][lang]["name"],
                            zones[current_zone_id][lang]["text"],
                            zones[current_zone_id][lang]["image"],
                            zones[current_zone_id][lang]["options"])

        # cargar imagen


        template_values = {
            "zone_title": current_zone.name,
            "zone_text": current_zone.text,
            "zone_img": current_zone.image,
            "zone_buttons": current_zone.options,
            "main_menu": main_menu_fields[lang],
            "pollen_percent": user.pollen,
            "pollen": pollen_fields[lang]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("zone.html",**template_values))