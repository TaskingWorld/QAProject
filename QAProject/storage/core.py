from tinydb import TinyDB


class Storage(object):

    def __init__(self, dbname: str):
        if (dbname.lower().endswith('.json')):
            self.db = TinyDB(dbname)
        else:
            self.db = TinyDB(dbname + '.json')

    def save(self, data: dict):
        self.db.insert(data)

    def find(self) -> list:
        return self.db.all()

    def drop(self):
        self.db.purge()