#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Course Project
#
from util import *
import random


#create gnomes g1,g2,... and save it as g1.fasta,g2.fasta,.... in fasta_dir/references
def generateDataset(num_gnomes, fasta_dir):
	for i in range(1,num_gnomes+1):
		n = random.randint(50000, 100000)
		fasta_out = getRefFile(fasta_dir, i)
		random_dna(n, i, fasta_out)

# create all read sets for a dataset
def generateReads(fasta_dir, settings, add_error=False):
	reads_sets = settings['reads_sets']
	for reads_set_id, reads_set in reads_sets.items():
		coverages = reads_set['coverages']
		for gnome_id, coverage in coverages.items():
			ref_file = getRefFile(fasta_dir, gnome_id)
			header_info, dna = read_dna_fasta(ref_file)

			fasta_out = getReadFile(fasta_dir, reads_set_id,  gnome_id)
			read_length = random.randint(settings['read_min_length'], settings['read_max_length'])

			#print(coverage)

			generateRandomReads(dna, read_length, coverage, fasta_out, add_error)


if __name__ == '__main__':
	pass
	#generateDataset(2, 'data/dataset1/')
	#generateDataset(8, 'data/dataset2/')
	#generateDataset(64, 'data/dataset3/')