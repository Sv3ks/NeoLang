from sys import argv
from lexer import lexer

if __name__ == '__main__':
	content = open(argv[1]).read()
	tokens = lexer(content)
	print(tokens)