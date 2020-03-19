from tinydb import TinyDB, Query

from QAProject.storage.core import Storage
from QAProject.actividad.core import Actividad

class TinyStorage(Storage):

    def __init__(self, dbname: str):
        if (dbname.lower().endswith('.json')):
            self.db = TinyDB(dbname)
        else:
            self.db = TinyDB(dbname + '.json')

        self.activities = self.db.table('activities')

    def save_activity(self, data: dict):
        self.activities.insert(data)

    def get_activities(self):
        return self.activities.all()
        
    def eliminate_activity(self, actividad: Actividad):
        query = Query()
        activity_name = actividad.nombre
        self.activities.remove(query.name == activity_name)