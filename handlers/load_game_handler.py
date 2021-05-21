# handler para cargar una partida previa

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
import webapp2
from webapp2_extras import jinja2

from classes.save import *
from classes.zone import zone

class load_game_handler(webapp2.RequestHandler):
    def post(self):
        # cargar usuario
        user = load_user()
        main_menu_fields = {"es": "Menu principal", "en": "Main menu"}
        pollen_fields = {"es": "Polen hostil en cavidad nasal", "en": "Hostile pollen in nasal cavity"}

        # cargar ultima zona visitada
        current_zone_id = user.zone

        from classes.zone_manager import zones
        lang = current_lang()

        # crear pagina
        current_zone = zone(zones[current_zone_id][lang]["name"],
                            zones[current_zone_id][lang]["text"],
                            zones[current_zone_id][lang]["image"],
                            zones[current_zone_id][lang]["options"])

        template_values = {
            "zone_title": current_zone.name,
            "zone_text": current_zone.text,
            "zone_img": current_zone.image,
            "zone_buttons": current_zone.options,
            "main_menu": main_menu_fields[lang],
            "pollen_percent": user.pollen,
            "pollen": pollen_fields[lang]
        }

        zone_buttons = zone.options
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("zone.html",**template_values))