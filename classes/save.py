# clases y funciones para gestion del guardado de entidades

from google.appengine.ext import ndb
from google.appengine.api import users
import time

# guardado de usuarios
class userSave(ndb.Model):
    id = ndb.StringProperty(required=True)
    zone = ndb.StringProperty(required=True)
    lang = ndb.StringProperty(required=True)
    pollen = ndb.FloatProperty(required=True)

def load_user():
    current_user = users.get_current_user()
    query = userSave.query(userSave.id == current_user.user_id())

    if query.count() == 0:
        # crear valores por defecto si no hay datos sobre el usuario actual
        aux = userSave()
        aux.id = current_user.user_id()
        aux.zone = "intro"
        aux.lang = "es"
        aux.pollen = 20
        aux.put()
        time.sleep(1)
        query = userSave.query(userSave.id == current_user.user_id())

    loaded = [i for i in query][0]
    return loaded

def delete_user_data(user):
    ndb.delete_multi([user.key])

def save_user(user):
    delete_user_data(user)
    user.put()

def current_lang():
    current_user = users.get_current_user()
    query = userSave.query(userSave.id == current_user.user_id())

    if query.count() == 0:
        # crear valores por defecto si no hay datos sobre el usuario actual
        aux = userSave()
        aux.id = current_user.user_id()
        aux.zone = "intro"
        aux.lang = "es"
        aux.pollen = 20
        aux.put()
        time.sleep(1)
        query = userSave.query(userSave.id == current_user.user_id())

    loaded = [i for i in query][0]
    return loaded.lang

def change_lang():
    current_language = current_lang()
    current_user = load_user()

    if current_language == "es":
        current_user.lang = "en"
    else:
        current_user.lang = "es"

    current_user.put()