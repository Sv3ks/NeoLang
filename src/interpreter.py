from sys import argv
from lexer import lex
from modulehandler import get_functions
from patternhandler import extract_pattern, extract_inputs

if __name__ == '__main__':

	functions = get_functions()

	content = open(argv[1]).read()
	tokens = lex(content)

	#print(extract_pattern(tokens[0]))
	#print(str(extract_inputs(tokens[0])))

	for line in tokens:
		pattern = extract_pattern(line)
		for function in functions:
			for function_pattern in function[1]:
				if function_pattern == pattern:
					function[0].Parse(str(extract_inputs(tokens[0])))