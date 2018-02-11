import os
import zipfile
from os import listdir
from os.path import isfile, join
import ReadableInformationFile

class PAR:
	def __init__(self, path):
		self.PATH = path

	def look_for(self, path, to_look_for):
		r = ReadableInformationFile.ReadableInformationReader(path)
		return r.get("main")

	def write_par(self, par_name):
		zipf = zipfile.ZipFile(par_name+".par", 'w', zipfile.ZIP_DEFLATED)
		files = [f for f in listdir(self.PATH) if isfile(join(self.PATH, f))]
		for file in files:
			if(file.endswith(".py") == True):
				zipf.write(file)

	def unzip_par(self,target_dir):
		with zipfile.ZipFile(self.PATH, 'r') as zipr:
			zipr.extractall(target_dir)
