import io
import sys
import csv
from configReader import ConfigReader


class FileReader:
		
	def readHeader(self):
		configReader = ConfigReader()
		config = configReader.readConfig()
		file = config.get('Csv', 'csv.file')
		topOffset = config.get('Csv','csv.topOffset')
		
		with open(file, "rb") as csvfile:
			file = csv.reader(csvfile, delimiter=',', quotechar='"')
			data = []
			for lines in file:
				data.append(lines)
			columns = data[int(topOffset)]		
		
		return columns
		
