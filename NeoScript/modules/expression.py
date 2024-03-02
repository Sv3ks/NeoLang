class Function:
	def __init__(self):
		self.patterns = []

		def parser(args):
			return 'Function does not have parser.'

		self.parse = parser
	def Parse(self, args):
		return self.parse(args)
	def Patterns(self):
		return self.patterns