import os
import sys

sys.dont_write_bytecode = True
dir = os.getcwd()
prefix = '$'
run = True

# Run Main Loop (only if __name__ is __main__)
if __name__ == '__main__':
	# Initialize Commands
	commands = []

	for filename in os.listdir("src/commands"):
		if filename.endswith(".py"):
			module = filename.removesuffix('.py')
			cmdClass = module.capitalize()
			exec(f'from commands.{module} import {cmdClass}')
			commands.insert(0, eval(f'{cmdClass}()'))

	print('Welcome to Patrick')
	print('Use help for more information')

	while run:
		# Get input
		userInput = input(f'{dir} {prefix} ')
		sortedInput = userInput.split(' ')
		
		# Get command name (first in sorted input)
		cmdName = sortedInput[0]
		
		# Get commands args (sorted input without command name)
		cmdArgs = sortedInput
		cmdArgs.remove(cmdName)

		for command in commands:
			if command.Name() == cmdName:
				command.Execute(cmdArgs)

		if userInput == 'exit':
			run = False