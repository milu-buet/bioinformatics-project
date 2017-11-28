from aligner import *
from settings import settings, datasets
from util import *

def classify(short_read, id, exact=True):
	alg = Aligner(datasets[id]['root'])
	alg.setIndexedGnomes(range(1, datasets[id]['gnomes']+1))

	if exact==True:
		return alg.AlignExatcly(short_read)[0]
	else:
		return 0

def get_reads(dataset_id,readset,gnome):
	fasta_dir = 'data/dataset' + str(dataset_id) + '/'
	filename = getReadFile(fasta_dir, readset, gnome)
	return read_randomRead_fasta(filename)

#Begin: Q6----------------------------------------------------------------
def runExperiment1_by_Dataset_Readset(dataset_id,readset):
	gnomes = datasets[dataset_id]["gnomes"]
	#total_reads = 0
	tp,fp,fn = 0,0,0


	#print(gnomes)
	for gnome in range(1,gnomes+1):
		reads = get_reads(dataset_id,readset,gnome)
		print(len(reads))
		for id,read in reads.items():
			#print(read)
			result = classify(read, dataset_id)
			#total_reads+=1
			if result == gnome:
				tp+=1
				#print("MIss\n")
			elif result == None:
				fn+=1
			elif result != gnome:
				fp+=1
	return tp,fp,fn


def runExperiment1_by_Dataset(dataset_id):
	
	tp1,fp1,fn1 = runExperiment1_by_Dataset_Readset(dataset_id,1)
	print(tp1,fp1,fn1)
	return tp1,fp1,fn1
	#tp2,fp2,fn2 = runExperiment1_by_Dataset_Readset(dataset_id,2)
	#print(tp2,fp2,fn2)

	#print("Dataset %s is done!"%(dataset_id))

	#return tp1+tp2,fp1+fp2,fn1+fn2


def runExperiment1():
	print('running ...')
	tp1,fp1,fn1 = runExperiment1_by_Dataset(1)
	print(tp1,fp1,fn1)
	print('ended ...')


runExperiment1()
#----------------------------------------------------------------