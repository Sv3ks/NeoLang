def tokenize(content):
	chars = list(content)
	result = "['"
	#temp = ''

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

	return eval(result)

print(tokenize('hello (hello again (and again) same here) and here...'))