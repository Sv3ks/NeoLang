from os import listdir

def get_functions():
	functions = []

	for filename in listdir("modules/functions"):
		if filename.endswith(".py"):
			module = filename.removesuffix('.py')
			functionClass = module.capitalize()
			# Import Function
			exec(f'from modules.functions.{module} import {functionClass}')

			# Add function class to list
			functions.append(eval(f'{functionClass}()'))
	
	return functions