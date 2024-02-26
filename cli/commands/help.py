from command import Command
import os

class Help(Command):
	def Execute(self, args):
		print('List of commands:')

		commands = []

		for filename in os.listdir("src/commands"):
			if filename.endswith(".py"):
				module = filename.removesuffix('.py')
				cmdClass = module.capitalize()
				exec(f'from commands.{module} import {cmdClass}')
				commands.insert(0, eval(f'{cmdClass}()'))

		for command in commands:
			print(f'Name: {command.Name()} - Usage: {command.Usage()} - Description: {command.Description()}')
	def Name(self):
		return 'help'
	def Description(self):
		return 'Shows a list of all commands and their information.'
	def Usage(self):
		return 'help'