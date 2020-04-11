# Obedient Oatmeal
# Chris Graham, 2020
# https://github.com/oishiiburger/obedientoatmeal
#
# A fun script for generating band names.

import random, csv

def printError(errorType):
	errors = {
		'IO': 'Required file not present'
	}
	print ('Error: '+errors.get(errorType))
	quit()

def readFile(filename):
	output = []
	try:
		with open(filename+".csv") as file:
			reader = csv.reader(file, \
			delimiter = ',')
			for row in reader:
				output.extend(row)
	except IOError:
		printError('IO')
	return output

def generateName(lg):
	adj = readFile('adj')
	noun = readFile('noun')
	name = ''
	for i in range(0, lg):
		if i==0 and lg==1:
			name += noun[random.randrange(0,len(noun)-1)].capitalize()
		elif i<lg-1:
			r = random.randrange(0,1)
			if r == 0:
				name += adj[random.randrange(0,len(adj)-1)].capitalize()
			else:
				name += noun[random.randrange(0,len(noun)-1)].capitalize()
		else:
			name += noun[random.randrange(0,len(noun)-1)].capitalize()
		if i != lg-1:
			name += ' '
	return name

def main():
	lg = random.randrange(1,5)
	print(generateName(lg))

if __name__ == "__main__":
	main()
