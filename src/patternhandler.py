def extract_pattern(tokens):
	pattern = ''

	for token in tokens:
		if isinstance(token,tuple):
			pattern += token[1]
		else:
			pattern += ' $ '

	return pattern

def extract_inputs(tokens):
	args = []

	for token in tokens:
		if isinstance(token,list):
			args += token

	return args
	# [('string','print'),[('string','Hello, World!')]]