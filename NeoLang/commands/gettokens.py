# Utils
from os import path, getcwd

# Internal
from NeoLang.interpreter import tokenize_content

def gettokens(args):
	content = open(f'{path.abspath(getcwd())}/{args[0]}').read()
	print(tokenize_content(content))