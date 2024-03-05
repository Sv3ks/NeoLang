from json import loads

class Package:
	def __init__(self, path):
		infof # package-info.json file
		try:
			infof = open(f'{path}\\package-info.json')
		except:
			print(f'ERROR LOADING PACKAGE - NO PACKAGE INFO FOUND: {path}')
			return
		
		info = loads(infof) # info = json loaded package-info.json
		
		self.info = info		
		self.dir = dir