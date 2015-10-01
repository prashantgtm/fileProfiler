from fileReader import FileReader
from tableMetadata import TableMetadata

class FileProfiler:

	def __init__(self):	
		fileReader = FileReader()
		tableMetadata = TableMetadata()
		fileColumns = fileReader.readHeader()
		dbColumns = tableMetadata.readMetadata()

		for i in range (len(fileColumns)):
			if fileColumns[i] <> dbColumns[i]:
				print "Error"
		print "All gud"

			
fileProfiler = FileProfiler()