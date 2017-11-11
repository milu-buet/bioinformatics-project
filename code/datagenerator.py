# Lutfar
from util import *
import random

def generateDataset(num_gnomes, fasta_dir):
	for i in range(1,num_gnomes+1):
		n = random.randint(50000, 100000)
		fasta_out = getRefFile(fasta_dir, i)
		random_dna(n, i, fasta_out)


def generateReads(fasta_dir):
	ref_files = getFastaFiles(getRefDir(fasta_dir))
	for ref_file in ref_files:
		header_info, dna = read_dna_fasta(ref_file)
		fasta_out = getReadFile(fasta_dir, header_info['id'])
		read_length = random.randint(200, 300)
		generateRandomReads(dna, read_length, coverage, fasta_out)


if __name__ == '__main__':
	generateDataset(2, 'data/dataset1/')
	generateDataset(8, 'data/dataset2/')
	generateDataset(64, 'data/dataset3/')