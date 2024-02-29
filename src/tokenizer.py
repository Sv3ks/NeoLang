from patternhandler import extract_args, extract_pattern
from json import dumps
from re import match

def clean_arr(arr):
	cleaned_arr = []
	for item in arr:
		if isinstance(item,list):
			cleaned_arr.append(clean_arr(item))
		elif not item == '': # and not item == ' '
			cleaned_arr.append(item)
	
	return cleaned_arr

def str_to_type(string):
	type = ''
	value = ''

	if string.startswith('"'):
		if string.endswith('"'):
			type = 'string'
			value = string.removeprefix('"').removesuffix('"')
		else:
			print('ERROR - STRING IS MISSING END QUOTE')
	elif string in '+/*':
		type = 'expression'
		value = string
	elif match(r'[\d+.]+',string): #? Could also be r'[0-9.]+'?
		type = 'number'
		value = string
	elif match(r'[a-zA-Z ]+',string):
		type = 'name'
		value = string
	else:
		print('ERROR: COULDT NOT DETECT ANY TYPE FROM STRING')
	return { 'type': type, 'value': value}

def str_to_type_from_arr(arr):
	result = []
	for item in arr:
		if isinstance(item,str):
			result.append(str_to_type(item))
		else:
			result.append(str_to_type_from_arr(item))
	return result

def tokenize(content):
	chars = list(content)
	result = "['"

	quotes = 0
	in_par = 0

	for char in chars:
		if char == '"':
			quotes += 1
		if quotes % 2:
			in_quotes = True
		else:
			in_quotes = False
		
		if char == '(' and not in_quotes:
			result += "',['"
			in_par += 1
		
		elif char == ')' and not in_quotes:
			result += "'],'"
			in_par -= 1

		elif char == ' ' and not in_quotes and in_par >= 1:
			result += "','"

		else:
			result += char

	result += "']"
	result = eval(result)

	# Clean the list for empty strings ('')

	result = clean_arr(result)

	# Final Process: Turn splitted content into output

	"""
	Output needs to be
	{
		'pattern': 'PATTERN HERE'
		'args': ['EXAMPLE ARG1',['EXAMPLE ARG2','EXAMPLE ARG3']]
	}
	"""

	pattern = extract_pattern(result)
	args = extract_args(result)

	# Tokenizing args

	args = str_to_type_from_arr(args)

	result = {'pattern': pattern, 'args': args}

	# Return tokenized content
	return result

sample_code = 'hello ("this is a string" + 42 + name (a)) and here...'
print(dumps(tokenize(sample_code),sort_keys=False, indent=4))