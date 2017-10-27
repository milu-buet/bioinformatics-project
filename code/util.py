import random

def random_dna(n):
	return ''.join([ random.choice('ACGT') for i in range(n) ])

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

if __name__ == '__main__':
	# create/save a random DNA sequence of length 10000 and 100 reads of length 50
	chop_into_reads(10000, 100, 50, 'seq.fasta', 'reads.fasta')
