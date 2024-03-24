from NeoLang.commands.run import run
from NeoLang.commands.version import version
from NeoLang.commands.packages import packages
from NeoLang.commands.gettokens import gettokens
from NeoLang.commands.parsetokens import parsetokens

COMMANDS = {
	'run': run,
	'version': version,
	'packages': packages,
	'gettokens': gettokens,
	'parsetokens': parsetokens,
}