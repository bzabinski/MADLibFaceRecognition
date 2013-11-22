from DatabaseConnector import DatabaseConnector as dbc
from FaceConfig import *

myDBC = dbc()
db = myDBC.getDB()

#This table is for the PCA_Train function to output to
drop = db.prepare("DROP TABLE IF EXISTS result_table, result_table_mean")
pcaTrain = db.prepare("SELECT madlib.pca_train(CAST ($1 AS text), CAST ($2 AS text), CAST ($3 AS text), CAST ($4 AS int))")
drop()
pcaTrain('pixels', "result_table", "row_id", individualNumber)
