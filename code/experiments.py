#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Course Project
#
from aligner import *
from settings import settings, datasets
from util import *

#classify a short_read in a dataset=id, exactly or approximately
def classify(short_read, id, exact=True):
	alg = Aligner(datasets[id]['root'])
	alg.setIndexedGnomes(range(1, datasets[id]['gnomes']+1))

	if exact==True:
		return alg.AlignExatcly(short_read)[0]
	else:
		return alg.AlignApproximately(short_read)[0]

# get all reads of a readset in a dataset
def get_reads(dataset_id,readset,gnome):
	fasta_dir = 'data/dataset' + str(dataset_id) + '/'
	filename = getReadFile(fasta_dir, readset, gnome)
	return read_randomRead_fasta(filename)


def runExperiment_by_Dataset_Readset(dataset_id,readset, exact=True):
	gnomes = datasets[dataset_id]["gnomes"]
	#total_reads = 0
	tp,fp,fn = 0,0,0

	#print(gnomes)
	for gnome in [1,2]:
		reads = get_reads(dataset_id,readset,gnome)
		#print(len(reads))
		for id,read in reads.items():
			#print(read)
			result = classify(read, dataset_id, exact)
			#total_reads+=1
			if result == gnome:
				tp+=1
				#print("MIss\n")
			elif result == None:
				fn+=1
			elif result != gnome:
				fp+=1
	return tp,fp,fn


def runExperiment_by_Dataset(dataset_id, exact=True):

	exp_readsets = [1,2,3]
	tp,fp,fn = 0,0,0
	for rset in exp_readsets:
		tpn,fpn,fnn = runExperiment_by_Dataset_Readset(dataset_id,rset,exact)
		tp,fp,fn = tp+tpn,fp+fpn,fn+fnn

	return tp,fp,fn



# def runExperiment1():
# 	print('running ...')
# 	tp1,fp1,fn1 = runExperiment_by_Dataset(1,True)
# 	print(tp1,fp1,fn1)
# 	print('ended ...')


# runExperiment1()
#----------------------------------------------------------------