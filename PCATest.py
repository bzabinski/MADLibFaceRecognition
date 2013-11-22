from DatabaseConnector import DatabaseConnector as dbc
from PGMReader import PGMReader as pgmr
from FaceConfig import *
import sys

#Get the test image from arguments
person = sys.argv[1]
view = sys.argv[2]

myDBC = dbc()
db = myDBC.getDB()
pgm = pgmr()
byteArray = []

#This table stores the test data
drop = db.prepare("DROP TABLE IF EXISTS test_pixels")
create = db.prepare("CREATE TABLE test_pixels (\
                        row_id integer,\
                        row_vec double precision[]\
                        );\
                    ")
drop()
create()

inserter1 = db.prepare("INSERT INTO test_pixels VALUES ($1, $2)")
pgm.openFile(imagePath + str(person) + '/' + str(view) + '.pgm')
for k in range(0, imageWidth * imageHeight):
    givenByte = pgm.readByte()
    byteArray.append(givenByte)
    currentRow = 26
inserter1(
    currentRow,
    byteArray
    )
byteArray.clear()


#These tables are for the PCA_Project function to output to
drop = db.prepare("DROP TABLE IF EXISTS residual_table, result_summary_table, out_table")
pcaTest = db.prepare("SELECT madlib.pca_project(CAST ($1 AS text), CAST ($2 AS text), CAST ($3 AS text), CAST($4 AS text), CAST($5 AS text), CAST($6 AS text))")
drop()
pcaTest("test_pixels", "result_table", "out_table", "row_id", "residual_table", "result_summary_table")
