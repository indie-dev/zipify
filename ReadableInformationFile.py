class ReadableInformationWriter:
	def __init__(self, path):
		#Set the global PATH variable to path
		self.PATH = path
	def write(self, key, value):
		#Write the key and value to self.PATH
		file = open(self.PATH, "w")
		file.write("["+key+"] => "+value+"\n")
		file.flush()
		file.close()

class ReadableInformationReader:
	def __init__(self, path):
		#Set the global PATH variable to path
		self.PATH = path

	def get(self, key):
		#Get the value of the key from self.PATH
		file = open(self.PATH, "r")
		content = file.readline();
		char = ""
		for text in list(content):
			char += text

		if(("["+key+"] => ") in char):
			return char.replace("["+key+"] => ", "")
		else:
			return "Key not found"
