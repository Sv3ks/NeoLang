class Function:
	def __init__(self):
		self.patterns = []

		def parser(args):
			print('Function does not have parser.')

		self.parse = parser
	def Parse(self, args):
		self.parse(args)
	def Patterns(self):
		return self.patterns