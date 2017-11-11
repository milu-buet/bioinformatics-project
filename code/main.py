from aligner import *
from datagenerator import *

reference_dirs = ['data/dataset1/references/', 'data/dataset2/references/', 'data/dataset3/references/']
gnome_counts = [2,8,64]

def generateDataset():
	for i in len(gnome_counts):
		generateDataset(gnome_counts[i],dataset_dirs[i])

def createFMI():
	for reference_dir in reference_dirs:
		alg = Alligner()
		alg.BuildIndexes(reference_dir)

def classify(short_read, dataset_id):
	alg = Alligner()
	alg.setIndexedGnomes(range(1,gnome_counts[dataset_id]+1))
	return alg.AllignExatcly(short_read)[0]

