import MySQLdb
from dbConnection import DbConnection

class TableMetadata:

	def readMetadata (self):
		dbConnection = DbConnection()
		conn = dbConnection.dbConnect()
		
		cursor = conn.cursor()
		cursor.execute("select raw_column_field from test.data_validation where raw_column_field <> '';")
		dbColumns = cursor.fetchall()

		rawColumns =[]
		for eachColumn in dbColumns:
			eachColumn  = [x.strip(',') for x in eachColumn]
			rawColumns.append(eachColumn)	
		conn.close()
		
		columns = []
		for i in range (len(rawColumns)):
			 columns.append(rawColumns[i][0])
	
		return columns
	
		
		
	
	