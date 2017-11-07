#Q3

from util import *

def generateRandomReads(reference_gnome, read_length, coverage):
	reads = {}
	number_of_reads = int(coverage/read_length)
	for i in range(number_of_reads):
		j = random.randint(0, len(reference_gnome)-read_length)
		reads[j,read_length] = reference_gnome[j:j+read_length]

	return reads


def saveRandomReads(reads,reads_file):
		with open(reads_file, 'w') as reads_out:
			for (key,value) in reads.items():
				reads_out.write('> position: {}, length: {}\n'.format(key[0],key[1]))
				reads_out.write('{}\n'.format(value))


		
a = generateRandomReads("ANBANABNAB",3,6)
print(a)