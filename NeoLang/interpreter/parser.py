class Parser:
	def __init__(self, packages = [], tokens = []) -> None:
		self.packages = packages
		self.tokens = tokens
	def expression(self,token):
		'Parse expression and return output of expression'
	def args(self,token):
		'Parse arguments and return result of arguments'
		'example: 1+"hello" => "1hello"'
	def effect(self, token):
		'Parse and run effect'
		print(str(token))

	def parse(self):
		for token in self.tokens:
			if token['type'] == 'EFFECT':
				self.effect(token)

	def load_packages(self, packages):
		self.packages.extend(packages)
	
	def add_tokens(self, tokens):
		self.tokens.extend(tokens)