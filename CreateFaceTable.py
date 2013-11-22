from DatabaseConnector import DatabaseConnector as dbc
from PGMReader import PGMReader as pgmr
from FaceConfig import *

myDBC = dbc()
db = myDBC.getDB()
pgm = pgmr()
byteArray = []

#This table is for the PCA_Train function to use
drop = db.prepare("DROP TABLE IF EXISTS pixels")
create = db.prepare("CREATE TABLE pixels (\
                        row_id integer,\
                        row_vec double precision[]\
                        );\
                    ")
drop()
create()

#This table maps row ids to the person ids
drop = db.prepare("DROP TABLE IF EXISTS personids")
create = db.prepare("CREATE TABLE personids (\
                        row_id integer,\
                        person_id integer\
                        );\
                    ")
drop()
create()

inserter1 = db.prepare("INSERT INTO pixels VALUES ($1, $2)")
inserter2 = db.prepare("INSERT INTO personids VALUES($1, $2)")

for i in range(1, individualNumber + 1): #add one since we start at one
    for j in range(1, viewsNumber + 1):
        pgm.openFile(imagePath + str(i) + '/' + str(j) + '.pgm')
        for k in range(0, imageWidth * imageHeight):
            givenByte = pgm.readByte()
            byteArray.append(givenByte)
        currentRow = (i - 1) * individualNumber + (j - 1)
        inserter1(
                    currentRow,
                    byteArray
                )
        inserter2(
                    currentRow,
                    i
                )
        byteArray.clear()
        pgm.closeFile()
