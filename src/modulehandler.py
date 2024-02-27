from os import listdir

def get_functions():
	functions = []

	for filename in listdir("modules/functions"):
		if filename.endswith(".py"):
			module = filename.removesuffix('.py')
			functionClass = module.capitalize()
			# Import Function
			exec(f'from modules.functions.{module} import {functionClass}')

			# Get Function Class
			function_class = eval(f'{functionClass}()')
			# Get Patterns From Class
			function_patterns = function_class.Patterns()

			# Add function to list
			functions.append((function_class, function_patterns))
	
	return functions