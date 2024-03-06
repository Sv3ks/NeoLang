import sys
sys.dont_write_bytecode = True
from json import dumps
from syntax.pipe import get_packages
from interpreter.tokenizer import tokenize

if __name__ == '__main__':
	sample_code = open('./examples/hello-world.ns').read()
	f = open('output.json','w')
	f.write(dumps(tokenize(sample_code),sort_keys=False, indent=4))
	#print(get_packages())