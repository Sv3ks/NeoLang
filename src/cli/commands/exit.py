from command import Command
import main

class Exit(Command):
	def Execute(self, args):
		print('Exiting...')
		main.run = False
	def Name(self):
		return 'exit'
	def Description(self):
		return 'Exits the console.'
	def Usage(self):
		return 'exit'