import re

def cleanText(text):
	return text.removeprefix(' ').removesuffix(' ')

def tokenize(content):
	def first_sort(string):
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
				result.append(cleanText(temp_str))
				temp_str = ''
			elif char == ')' and not in_quotes:
				result.append(first_sort(temp_str))
				temp_str = ''
			else:
				temp_str += char

		result.append(cleanText(temp_str))
		return result



	lines = content.split('\n')
	for line in lines:
		# First Sorting (Splitting Parenthesis)
		tokens = first_sort(line)
	
		# Second Sorting (Sorting Data Types)
		items = []
		for token in tokens:
			# Strings
			if token == '':
				continue
			elif token[0] == '"':
				if token[-1] == '"':
					items.append(('string', token))
				else:
					# ERROR
					print('Error... :(')
			# Functions
			elif re.match(r'[.a-zA-Z]+', token):
				items.append(('symbol',token))
			# Expressions
			elif token in '+-/*':
				items.append(('expression',token))
			# Number
			elif re.match(r'[.0-9]+',token):
				items.append(('number',token))


		print(items)
		print(tokens)

if __name__ == '__main__':
	contents = open('../examples/hello-world.pk').read()
	tokenize(contents)