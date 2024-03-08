import sys
sys.dont_write_bytecode = True
from syntax.pipe import get_packages
from interpreter.tokenizer import tokenize_content
from interpreter.parser import Parser

if __name__ == '__main__':
	sample_code = open('./examples/hello-world.ns').read()
	
	parser = Parser()
	
	#* Load and feed packages to Parser
	packages = get_packages()
	parser.load_packages(packages)

	#* Tokenize file and feed tokens to Parser
	tokens = tokenize_content(sample_code)
	parser.add_tokens(tokens)

	#* Parse everything
	parser.parse()

	#f = open('output.json','w')
	#f.write(dumps(tokenize(sample_code),sort_keys=False, indent=4))