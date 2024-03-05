from os import listdir
from classes.package import Package

def get_packages():
	packages = []
	dir = './NeoScript/syntax/packages'
	for package in listdir(dir):
		packages.append(Package(f'{dir}/{package}'))
	
	return packages