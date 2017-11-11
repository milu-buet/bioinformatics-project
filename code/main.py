from aligner import *
from datagenerator import *


settings = {
	'gnome_min_length': 50000,
	'gnome_max_length': 100000,
	'read_min_length': 200,
	'read_max_length': 300,
	'error': 0.0,
	"reads": {
			1: {
				'coverage': {
				    1: 1,
				    2: 2
				}
			},

			2: {
				'coverage': {
				    1: 2,
				    2: 4
				}
			}

		}

}

datasets = {
	1: {
		"root": 'data/dataset1/',
		"gnomes": 2,
		
	},
	2: {
		"root": 'data/dataset2/',
		"gnomes": 8,
	},
	3: {
		"root": 'data/dataset3/',
		"gnomes": 64,
	}
}


def createDataset(id):
	print(datasets[id])
	generateDataset(datasets[id]['gnomes'],datasets[id]['root'])


def createFMI(id):
	alg = Aligner(datasets[id]['root'])
	alg.BuildIndexes()

def classify(short_read, id):
	alg = Aligner(datasets[id]['root'])
	alg.setIndexedGnomes(range(1, datasets[id]['gnomes']+1))
	return alg.AlignExatcly(short_read)[0]

def createDatasets():
	print('Creating dataset 1 ....')
	createDataset(1)
	print('Creating FMI for dataset 1 ....')
	createFMI(1)
	print('completed dataset 1 ....')

	print('Creating dataset  2....')
	createDataset(2)
	print('Creating FMI for dataset 2 ....')
	createFMI(2)
	print('completed dataset 2 ....')

	print('Creating dataset  3....')
	createDataset(3)
	print('Creating FMI for dataset 3 ....')
	createFMI(3)
	print('completed dataset 3 ....')

if __name__ == '__main__':
	
	#createDatasets()  #one time run

	on_dataset = 3 
	result = classify("ATGCATAAAAAT", on_dataset)
	print(result)



