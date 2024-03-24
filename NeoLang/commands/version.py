from pkg_resources import get_distribution

def version(args):
	v = get_distribution('neolang').version
	print(f'You are currently running NeoLang version {v}.')