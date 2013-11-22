import postgresql as pg

class DatabaseConnector:
    def __init__(self):
        self._db = pg.open("pq://testuser:testPassword@localhost/madlibdb")
        self._db.connect()
    def getDB(self):
        return self._db
