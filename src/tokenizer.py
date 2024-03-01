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
			type = 'STRING'
			value = string.removeprefix('"').removesuffix('"')
		else:
			print('ERROR - STRING IS MISSING END QUOTE')
	elif string in '+-*/':
		type = 'OPERATOR'
		value = string
	elif match(r'[\d+.]+',string): #? Could also be r'[0-9.]+'?
		type = 'NUMBER'
		value = string
	elif match(r'[a-zA-Z ]+',string):
		type = 'NAME'
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

def define_expressions(args):
	result = []
	in_expr, temp_pattern

	in_expr = False
	temp_pattern = []

	# Iterate through args
	for i in range((len(args))):
		if isinstance(args[i],dict) and args[i]['type'] == 'NAME':
			in_expr = True
			temp_pattern += args[i]['value'] + ' '
		elif isinstance(args[i],list):
			in_expr = True
			temp_pattern += '$ '
			temp_args.append()

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

	pattern = extract_pattern(result)
	args = extract_args(result)

	# Merging multiple names into expression

	#args = define_expressions(args)

	# Tokenizing args

	args = str_to_type_from_arr(args)

	#TODO Iterate through args and check for names. Names and args belonging to names should be formatted as an expression.

	result = {'type': 'FUNCTION', 'pattern': pattern, 'args': args}

	# Return tokenized content
	return result

sample_code = open('./src/test.ns').read()
f = open('output.json','w')
f.write(dumps(tokenize(sample_code),sort_keys=False, indent=4))