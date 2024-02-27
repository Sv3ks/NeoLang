import re

def clean_str(string):
	return string.removeprefix(' ').removesuffix(' ')

def split_par(string):
	chars = list(string)
	result = []
	temp_str = ''
	quoute_count = 0
	for char in chars:
		# Quote Stuff
		if char == '"':
			quoute_count += 1
		if quoute_count % 2 == 0:
			in_quotes = False
		else:
			in_quotes = True


		# Split Paranthesis
		if (char == '(' or char == ' ') and not in_quotes:
			result.append(clean_str(temp_str))
			temp_str = ''
		elif char == ')' and not in_quotes:
			result.append(split_par(temp_str))
			temp_str = ''
		else:
			temp_str += char
	
	result.append(clean_str(temp_str))
	return result

def split(string):
	chars = list(string)
	result = []
	temp_str = ''
	quoute_count = 0
	for char in chars:
		# Quote Stuff
		if char == '"':
			quoute_count += 1
		if quoute_count % 2 == 0:
			in_quotes = False
		else:
			in_quotes = True


		# Split Paranthesis
		if char == '(' and not in_quotes:
			result.append(clean_str(temp_str))
			temp_str = ''
		elif char == ')' and not in_quotes:
			result.append(split_par(temp_str))
			temp_str = ''
		else:
			temp_str += char

	result.append(clean_str(temp_str))
	return result

def tokenize(field):
	if field[0] == '"':
		if field[-1] == '"':
			return ('string', field.removeprefix('"').removesuffix('"'))
		else:
			# ERROR
			return ('Error... :(')
	# Functions
	elif re.match(r'[.a-zA-Z]+', field):
		return ('symbol',field)
	# Expressions
	elif field in '+-/*':
		return ('expression',field)
	# Number
	elif re.match(r'[.0-9]+',field):
		return ('number',field)
	# None :(
	else:
		return ('Error... :(')

def tokenize_arr(arr):
	tokens = []
	for field in arr:
		#print(field)
		# Check If Token Is String Or Array
		if str(field) == field:
			# Make sure field is not empty
			if not field == '':
				tokens.append(tokenize(field))
		# It's an Array
		else:
			tokens.append(tokenize_arr(field))
	return tokens



def lexer(content):
	lines = content.split('\n')
	result = []
	for line in lines:
		# First Sorting (Splitting Into Fields)
		fields = split(line)

		# Second Sorting (Tokenizing Fields)
		tokens = tokenize_arr(fields)

		result.append(tokens)

	return result