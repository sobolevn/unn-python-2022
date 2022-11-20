import argparse
from argparse import *
from commands import *

my_commands = {'highligh':DoHighlight,'cowsay':DoCowSay,'time':DoTime}

def myinput():
	parser = argparse.ArgumentParser(description='My example explanation')
	parser.add_argument('first',type = str,help = "highligh/cowsay/Time")
	parser.add_argument('second',type = str,help = "highligh:Text,cowsay:Text,Time:Region/City")
	names = parser.parse_args()

	what_do(names)

def what_do(dat):

	try:
		my_commands[dat.first](dat.second)
	except Exception as ex:
		_help()
		print("Errore!!! first: {0} second: {1}".format(dat.first,dat.second))
	
	
def _help():
	print("highligh: input python code")
	print("cowsay: input text")
	print("time: Region/City")


