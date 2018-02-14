# File: commandLineTools.py
# Author: Ariana Jorgensen
# Description: This program uses argparse to perform simple 
#			   tasks
# Notes: To see full functionality, run program using syntax
# 'python ./commandLineTools.py -h' 

import argparse
import datetime 


def getArgs():
	
	parser = argparse.ArgumentParser(description='Basic command line program')

	parser.add_argument('-f', '--file', action='store_true', help='Writes results to a file (must provide a file name)')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-g', '--greet', action='store_true', help='Print generic greeting')
	group.add_argument('-c', '--custom', nargs='?', help='Print customized greeting')
	group.add_argument('-l', '--love', nargs='?', help='Hear that you are loved')
	group.add_argument('-j', '--joke', action='store_true', help='Hear a joke')
	group.add_argument('-t', '--time', action='store_true', help='Get time')
	group.add_argument('-d', '--date', action='store_true', help='Get date')


	return parser.parse_args()

def makeFile(filename, result):

	newFile = open(filename + ".txt", "w+")
	newFile.write(result + "\n")
	newFile.close()


def processArgs(args):

	if args.greet:
		result = "Hello!"
	elif args.custom:
		result = "Hello, "+ args.custom
	elif args.love:
		result = "I love you, "+ args.love
	elif args.joke:
		result = "I would tell you a UDP joke, but you might not get it"
	elif args.time:
		t = datetime.datetime.now()
		result = t.strftime("%I:%M:%S %p")
	elif args.date:
		t = datetime.datetime.now()
		result = t.strftime("%Y/%m/%d")


	if args.file:
		makeFile(args.file, result)
	
	return result


def main():
	args = getArgs()
	print(processArgs(args))

if __name__ == '__main__':
	main()





# basic-python-comman-line-tool-ari-jorgensen
