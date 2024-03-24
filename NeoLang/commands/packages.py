from NeoLang.syntax import get_packages

def packages(args):
	print('Here is a list of all installed NeoLang Packages:')
	for package in get_packages():
		print(f' - {package.name}')