# Obedient Oatmeal
# Chris Graham, 2020
# https://github.com/oishiiburger/obedientoatmeal
#
# A fun script for generating band names from
# nouns and adjectives parsed from plaintext input files

import chardet, codecs, nltk, os, random, string, sys

def printError(errorType):
	errors = {
		'Args'	: 'You must specify a text file to parse.\n'+\
				  'Usage: (python) obedientoatmeal.py filename_to_parse [number of band names]',
		'Decode': 'Could not successfully detect file encoding.',
		'IO'	: 'File not found or IO error.',
		'Type'	: 'Argument is of improper type.'
	}
	print ('Error: '+errors.get(errorType))
	quit()

def updateProgress(iteration, total):
	print('Working... '+str(int((iteration / total) * 100)) + "%", end='\r', flush=True)

def readFile(filename):
	try:
		file = open(filename, 'rb')
		output = file.read()
		codec = chardet.detect(output).get('encoding')
		output = output.decode(codec)
		size = os.path.getsize(filename)
		file.close()
	except IOError or OSError:
		printError('IO')
	except UnicodeDecodeError:
		printError('Decode')
	print('Parsing ' + filename + ', ' + str(size//1000) + 'kb')
	return output

def generateName(filename, number):
	text = readFile(filename)
	sents = nltk.sent_tokenize(text)
	nouns = []
	adjs = []
	sents_length = len(sents)
	# tokenize while excluding punctuation
	# tag each word in each of the sentences
	# append lists with unique nouns and adjs
	tokenizer = nltk.RegexpTokenizer(r"\w+")
	for i,sent in enumerate(sents):
		updateProgress(i, sents_length)
		for tag_tuple in nltk.pos_tag(tokenizer.tokenize(sent)):
			if len(tag_tuple[0]) > 1:
				if tag_tuple[1] == 'NN':
					if tag_tuple[0] not in nouns:
						nouns.append(tag_tuple[0])
				elif tag_tuple[1] == 'JJ':
					if tag_tuple[0] not in adjs:
						adjs.append(tag_tuple[0])
	print('\n')
	for i in range(0, number):
		# change range below for shorter or longer band names
		length = random.randrange(2,4)
		name = ''
		for i in range(0, length):
			if i==0 and length==1:
				name += nouns[random.randrange(0,len(nouns)-1)].capitalize()
			elif i<length-1:
				r = random.randrange(0,1)
				if r == 0:
					name += adjs[random.randrange(0,len(adjs)-1)].capitalize()
				else:
					name += nouns[random.randrange(0,len(nouns)-1)].capitalize()
			else:
				name += nouns[random.randrange(0,len(nouns)-1)].capitalize()
			if i != length-1:
				name += ' '
		print(name)

def main():
	# see if punkt is already installed
	# prompt to install it if not
	try:
		nltk.data.find('tokenizers/punkt')
		nltk.data.find('taggers/averaged_perceptron_tagger.zip')
	except LookupError:
		print("NLTK 'punkt' or 'averaged_perceptron_tagger' is not installed.")
		yn = input("Install it now? [y]es, [n]o, [i]gnore: ")
		if yn != 'y' and yn != 'i':
			quit()
		elif yn != 'i':
			nltk.download('punkt')
			nltk.download('averaged_perceptron_tagger')
		else:
			pass
	try:
		if len(sys.argv) < 2 or len(sys.argv) > 3:
			printError('Args')
		elif len(sys.argv) == 2:
			generateName(sys.argv[1], 1)
		else:
			generateName(sys.argv[1], int(sys.argv[2]))
	except ValueError:
		printError('Type')

if __name__ == "__main__":
	main()
