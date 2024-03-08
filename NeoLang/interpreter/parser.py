class Parser:
	def __init__(self, packages = [], tokens = []) -> None:
		self.packages = packages
		self.tokens = tokens
	def effect(self, token):
		''

	def parse(self):
		for token in self.tokens:
			if token['type'] == 'EFFECT':
				self.effect(token)

	def load_packages(self, packages):
		self.packages.extend(packages)
	
	def add_tokens(self, tokens):
		self.tokens.extend(tokens)