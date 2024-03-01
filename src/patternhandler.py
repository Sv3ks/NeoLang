 # TODO: Move patternhandler.py -> tokenizer.py reasoned that it is simply the place for it :) 

def extract_pattern(tokens):
	pattern = ''

	for token in tokens:
		if isinstance(token,str):
			pattern += token
		else:
			pattern += '$'

	return pattern

def extract_args(tokens):
	args = []

	for token in tokens:
		if isinstance(token,list):
			args += token

	return args