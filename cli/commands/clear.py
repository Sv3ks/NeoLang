from command import Command
from os import system, name

class Clear(Command):
	def Execute(self, args):
		if name == 'nt':
			system('cls')
		elif name == 'posix':
			system('clear')
		else:
			print('UNKNOWN SYSTEM')
	def Name(self):
		return 'clear'
	def Description(self):
		return 'Clears the console.'
	def Usage(self):
		return 'clear'