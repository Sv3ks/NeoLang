# Get rid of pycache
import sys
sys.dont_write_bytecode = True

# Internal
from neolang.commands import COMMANDS

def cli():
	args = sys.argv
	args.pop(0)
	if args == []:
		print('Hello from NeoLang!')
		return
	
	for command in COMMANDS:
		if args[0].lower() != command.lower(): continue
		args.pop(0)
		COMMANDS[command](args)
		return

if __name__ == '__main__':
	cli()