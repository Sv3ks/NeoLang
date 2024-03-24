from NeoLang.commands.run import run
from NeoLang.commands.version import version
from NeoLang.commands.packages import packages
from NeoLang.commands.gettokens import gettokens

COMMANDS = {
	'run': run,
	'version': version,
	'packages': packages,
	'gettokens': gettokens,
}