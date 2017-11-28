from aligner import *
from datagenerator import *
from settings import settings, datasets


def createDataset(id):
	#print(datasets[id])
	generateDataset(datasets[id]['gnomes'],datasets[id]['root'])

def createReadsSets(id, add_error=False):
	generateReads(datasets[id]['root'], settings, add_error)


def createFMI(id):
	alg = Aligner(datasets[id]['root'])
	alg.BuildIndexes()

def classify(short_read, id):
	alg = Aligner(datasets[id]['root'])
	alg.setIndexedGnomes(range(1, datasets[id]['gnomes']+1))
	return alg.AlignExatcly(short_read)[0]

def createDatasets(ids,d,f,r,add_error=False):
	for id in ids:
		if d==1:
			print('Creating dataset %s ....'%(id,))
			createDataset(id)
		if f==1:
			print('Creating FMI for dataset %s ....'%(id,))
			createFMI(id)
		if r==1:
			print('Creating reads for dataset %s ....'%(id,))
			createReadsSets(id,add_error)
		print('completed dataset %s ....'%(id,))




def run_experiment_and_report_Q6():
	pass




if __name__ == '__main__':
	
	createDatasets([1,],0, 0, 1, True)  #one time run

	on_dataset = 1
	result = classify("ATGCAAAAT", on_dataset)
	print(result)



