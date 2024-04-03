# Utils
from os import path, getcwd

# Internal
from neolang.syntax import *
from neolang.interpreter import *

def run(args):
	content = open(f'{path.abspath(getcwd())}/{args[0]}').read()

	parser = Parser()

	#* Load and feed packages to Parser
	packages = get_packages()
	parser.load_packages(packages)

	#* Tokenize file and feed tokens to Parser
	tokens = tokenize_content(content)
	parser.add_tokens(tokens)

	#* Parse everything
	parser.parse()