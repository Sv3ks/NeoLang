from modules.function import Function

class Print(Function):
	def __init__(self):
		super().__init__()

		self.patterns = [
			'print $ ',
			'print $ to console',
			'write $ to console',
			'send $ to console'
		]

		def parser(args):
			print(args)

		self.parse = parser