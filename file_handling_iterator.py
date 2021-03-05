from sys import argv

def readfile(filename):
	f = open(filename, mode='rt', encoding='utf-8')
	
	for line in f:
		print(line, end=' ')
	f.close()

if __name__ == '__main__':
	readfile(argv[1])