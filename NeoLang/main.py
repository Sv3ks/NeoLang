# Get rid of pycache
import sys
sys.dont_write_bytecode = True

# Internal
from NeoLang.commands import COMMANDS

def Main():
	args = sys.argv
	args.pop(0)
	for command in COMMANDS:
		if args[0].lower() != command.lower(): continue
		args.pop(0)
		COMMANDS[command](args)
		return