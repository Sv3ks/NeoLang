from .run import run
from .version import version
from .packages import packages
from .gettokens import gettokens
from .parsetokens import parsetokens

COMMANDS = {
	'run': run,
	'version': version,
	'packages': packages,
	'gettokens': gettokens,
	'parsetokens': parsetokens,
}