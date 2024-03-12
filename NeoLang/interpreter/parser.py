from interpreter.operator import Operator

class Parser:
	def __init__(self, packages = [], tokens = []) -> None:
		self.packages = packages
		self.tokens = tokens
	def parse_expr(self,token):
		#* Parse expression and return output of expression'
		pattern = token['pattern']
		for package in self.packages:
			for expression in package.expressions:
				if pattern in expression.patterns:
					return expression.parser(self.parse_args(token['args']))		
		#! NO EXPRESSION FOUND - THROW ERROR

	def parse_args(self,args):
		#* Parse arguments and return result of arguments
		
		clean_args = [] #? List containing args where expressions have been parsed

		for arg in args:
			if arg['type'] == 'EXPRESSION':
				clean_args.append(self.parse_expr(arg))
			else:
				clean_args.append(arg)
		
		stripped_args = [] #? List containing args where the datatypes is clarified (dict -> str/int/etc)

		for arg in clean_args:
			match arg['type']:
				case 'TEXT':
					stripped_args.append(str(arg['value']))
				case 'NUMBER':
					stripped_args.append(float(arg['value']))
				case 'OPERATOR':
					stripped_args.append(Operator(arg['value']))
				case _:
					pass #! NOT VALID DATATYPE - PRINT ERROR
		
		pattern = [] #? List containing datatypes excluding operators to figure out how to handle merging args (['hello', Operator('+'), 21] -> [str,float])
		operators = [] #? List containing all operators
		values = [] #? List containing all values 

	def parse_effect(self, token):
		'Parse and run effect'
		print(str(token))

	def parse(self):
		for token in self.tokens:
			if token['type'] == 'EFFECT':
				self.parse_effect(token)

	def load_packages(self, packages):
		self.packages.extend(packages)
	
	def add_tokens(self, tokens):
		self.tokens.extend(tokens)