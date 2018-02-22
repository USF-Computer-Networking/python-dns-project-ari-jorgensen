import socket
import argparse

def getArgs():

	parser = argparse.ArgumentParser(description='Simple DNS lookup')

	parser.add_argument('domain', nargs='+', help='Lookup IP addr of specified domain name')

	return parser.parse_args()

def lookup(args):

	for val in range (len(args.domain)):
		addr = socket.gethostbyname(args.domain[val])
		print(args.domain[val] + ": " + addr)


def main():
	args = getArgs()
	lookup(args)

if __name__ == '__main__':
	main()# python-dns-project-ari-jorgensen
