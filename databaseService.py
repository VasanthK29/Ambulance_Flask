from dbconnection import *

class JunctionTable:
    def __init__(self, id, jName, lat, lon):
        self.id = id
        self.junctionName = jName
        self.latitude = lat
        self.longitude = lon

class databaseService(dbDetection):
    def getTableJunction(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from junction")
        rows = []
        for x in cursor:
            rows.append(JunctionTable(*x))
        return rows