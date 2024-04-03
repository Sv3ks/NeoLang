# Utils
from os import path, getcwd

# Internal
from neolang.syntax import *
from neolang.interpreter import *

def parsetokens(args):
	tokens = open(f'{path.abspath(getcwd())}/{args[0]}').read()
	parser = Parser()
	packages = get_packages()
	parser.load_packages(packages)
	parser.add_tokens(tokens)
	parser.parse()