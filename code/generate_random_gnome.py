#Q2

from util import *



def generateRandomGnome(n, data_file):
	file = open(data_file , 'w')
	file.write(random_dna(n) + '\n')
	file.close()
	return 0

def loadRandomGnomeData(data_file):
	file = open(data_file, 'r')
	return file.read()
	



data_file = 'data/random_gnome.fasta'
generateRandomGnome(1000,data_file)
print(loadRandomGnomeData(data_file))