from aligner import *
from datagenerator import *
from settings import settings, datasets
from experiments import *
import time


def createDataset(id):
	#print(datasets[id])
	generateDataset(datasets[id]['gnomes'],datasets[id]['root'])

def createReadsSets(id, add_error=False):
	generateReads(datasets[id]['root'], settings, add_error)


def createFMI(id):
	alg = Aligner(datasets[id]['root'])
	alg.BuildIndexes()

def createDatasets(ids,d,f,r,add_error=False):
	for id in ids:
		if d==1:
			#print('Creating dataset %s ....'%(id,))
			createDataset(id)
		if f==1:
			#print('Creating FMI for dataset %s ....'%(id,))
			createFMI(id)
		if r==1:
			#print('Creating reads for dataset %s ....'%(id,))
			createReadsSets(id,add_error)
		#print('completed dataset %s ....'%(id,))

def show_report(dset,tp,fp,fn,runtime):
	
	if tp>0:
		precision = float(tp)/(tp+fp)
		recall = float(tp)/(tp+fn)
	else:
		precision = 0
		recall = 0
	print("Dataset%s: runtime: %s, precision: %s, recall: %s"% (dset,runtime,precision,recall,))



def runExperiment(exp_datasets, exact=True):
	
	for dset in exp_datasets:
		start = time.time()
		tp,fp,fn = runExperiment_by_Dataset(dset,exact)
		end = time.time()
		show_report(dset,tp,fp,fn,end-start)
		print("Experiment on dataset %s completed"%(dset,))



def runExperiment1(exp_datasets):
	print('Running experiment 1 (Alignexactly, No Error) ...')
	createDatasets(exp_datasets,0, 0, 1, False)
	runExperiment(exp_datasets,True)
	print('Experiment 1 ended ...')
	

def runExperiment2(exp_datasets):
	print('Running experiment 2 (Align exactly, 1 percent Error) ...')
	createDatasets(exp_datasets,0, 0, 1, True)
	runExperiment(exp_datasets,True)
	print('Experiment 2 ended ...')
		

def runExperiment3(exp_datasets):
	print('Running experiment 2 (Align approximately, 1 percent Error) ...')
	createDatasets(exp_datasets,0, 0, 1, True)
	runExperiment(exp_datasets,False)
	print('Experiment 2 ended ...')


def runExperiments():
	exp_datasets = [1,2,3]

	runExperiment1(exp_datasets)
	runExperiment2(exp_datasets)
	runExperiment3(exp_datasets)




if __name__ == '__main__':
	
	runExperiments()

