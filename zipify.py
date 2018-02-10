import os
import zipfile
from os import listdir
from os.path import isfile, join

class PAR:
	def __init__(self):
		pass

	def write_par(self,path, par_name):
		zipf = zipfile.ZipFile(par_name+".par", 'w', zipfile.ZIP_DEFLATED)
		files = [f for f in listdir(path) if isfile(join(path, f))]
		for file in files:
			if(file.endswith(".py") == True):
				zipf.write(file)
			print(file)

	def unzip_par(self,path,target_dir):
		with zipfile.ZipFile(path, 'r') as zipr:
			zipr.extractall(target)
