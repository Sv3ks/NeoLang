from sys import argv
from lexer import lex
from modulehandler import get_functions
from patternhandler import extract_pattern, extract_inputs

if __name__ == '__main__':

	functions = get_functions()

	content = open(argv[1]).read()
	tokens = lex(content)

	for line in tokens:
		pattern = extract_pattern(line)
		for function in functions:
			if pattern in function.Patterns():
				function.Parse(extract_inputs(tokens[0]))