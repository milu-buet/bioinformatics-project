import random

#generate random dna
#----------------------------------------------------------------------------
def random_dna(n, id = None, fasta_out = None):
	s = ''.join([ random.choice('ACGT') for i in range(n) ])
	if fasta_out is not None:
		with open(fasta_out, 'w') as f:
			f.write('> |id: {}|name: {}|length: {}|\n'.format(id,"g"+str(id),n))
			width = 60
			lines = [ s[i : i+width] for i in range(0, len(s), width) ]
			for line in lines:
				f.write('{}\n'.format(line))
	else:
		return s

#----------------------------------------------------------------------------
# Assuming there is only one sequence in the file.  In general, a FASTA file
# may have multiple sequences, separated by ">"
#----------------------------------------------------------------------------
def read_dna_fasta(filename):
	with open(filename, 'r') as f:
		header = f.readline().strip()
		header_info = getHeaderInfo(header)
		dna = ''.join([ s.strip() for s in f.readlines() ])
		return header_info, dna

def getHeaderInfo(header):
	info_dict = {}
	info_data = header.split('|')
	for data in info_data:
		if ":" in data:
			key,value = data.split(': ')
			info_dict[key] = value
	return info_dict


# generate random reads from reference gnome
def generateRandomReads(reference_gnome, read_length, coverage, fasta_out=None):
	reads = {}
	number_of_reads = int(coverage*(len(reference_gnome))/read_length)
	for i in range(number_of_reads):
		j = random.randint(0, len(reference_gnome)-read_length)
		reads[j,read_length] = reference_gnome[j:j+read_length]

	if fasta_out is not None:
		with open(fasta_out, 'w') as f:
			for (key,value) in reads.items():
				f.write('> position: {}, length: {}\n'.format(key[0],key[1]))
				f.write('{}\n'.format(value))
	return reads


# read randomRead fasta
def read_randomRead_fasta(filename):
	reads = {}
	with open(filename, 'r') as f:
		rawReads = f.read().split('\n')
		for i in range(len(rawReads)):
				if rawReads[i] and len(rawReads[i]) > 1 and rawReads[i][0] == '>':
					reads[i] = rawReads[i+1]
	return reads

#----------------------------------------------------------------------------
def mutate_one_base(seq, bases):
	options = list(bases)
	i = random.randint(0, len(seq)-1)
	if seq[i] in options:
		options.remove(seq[i])
	s = list(seq)
	s[i] = options[ random.randint(0, len(options)-1) ]
	return ''.join(s)

#----------------------------------------------------------------------------
'''
Create a random DNA sequence of length ref_seq_len
Create n random reads of length read_length
Ref sequence is saved to ref_seq_file
Reads are saved to reads_file
'''
def chop_into_reads(ref_seq_len, n, read_length, ref_seq_file, reads_file):
	seq = random_dna(ref_seq_len)
	with open(ref_seq_file, 'w') as seq_out:
		seq_out.write('> Reference sequence of length {}\n'.format(len(seq)))
		seq_out.write(seq)

	with open(reads_file, 'w') as reads_out:
		for i in range(n):
			j = random.randint(0, len(seq)-read_length)
			reads_out.write('> position: {}, length: {}\n'.format(j,read_length))
			reads_out.write('{}\n'.format(seq[j:j+read_length]))


def random_substr(seq, n):
	if n > len(seq):
		return none
	j = random.randint(0, len(seq)-n)
	return seq[j:j+n]

def getFastaFiles(direc):
	import glob
	#file_list = glob.glob("data/reference_gnomes/*.fasta")
	file_list = glob.glob(direc + "*.fasta")
	#print(file_list)
	return file_list

def getRefDir(fasta_dir):
	return fasta_dir + 'references/'

def getReadDir(fasta_dir):
	return fasta_dir + 'reads/'

def getFMIDir(fasta_dir):
	return fasta_dir + 'fmi/'

def getRefFile(fasta_dir, id):
	return getRefDir(fasta_dir) + "g"+str(id)+".fasta"

def getReadFile(fasta_dir, set_id, id):
	return getReadDir(fasta_dir) + str(set_id) + "/g"+str(id)+".fasta"

def getFMIFile(fasta_dir, id):
	return getFMIDir(fasta_dir) + "g"+str(id)+".pickle"



if __name__ == '__main__':
	# create/save a random DNA sequence of length 10000 and 100 reads of length 50
	# chop_into_reads(10000, 100, 50, 'seq.fasta', 'reads.fasta')
	# print(random_dna(250, "test.fasta"))
	# header, dna = read_fasta('test.fasta')
	# print(header, len(dna))
	# print(dna)
	# for i in range(20):
	# 	print(mutate_one_base('AAAAAAAAAAA', 'ACGT'))
	#reads = read_randomRead_fasta('data/reads.fasta')
	#print(reads)

	random_dna(100,1,'data/reference_gnomes/g1.fasta')
	file_list = getFastaFiles("data/reference_gnomes/")
	print(file_list)





