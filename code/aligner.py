# Md Lutfar Rahman
#Q4

from util import *
from fmi import *
import pickle


class Aligner():
	def __init__(self, fasta_dir):
		self.indexed_gnomes = []
		self.fasta_dir = fasta_dir

	def BuildIndex(self,header_info,reference_gnome):
		index = FMI(reference_gnome+'$')
		self.indexed_gnomes.append(header_info['id'])
		fmi_loc = getFMIFile(self.fasta_dir, header_info['id'])
		file = open(fmi_loc , 'wb')
		pickle.dump(index,file)
		return index

	def BuildIndexes(self):
		reference_gnome_files = getFastaFiles(getRefDir(self.fasta_dir))
		for reference_gnome_file in reference_gnome_files:
			header_info,dna = read_dna_fasta(reference_gnome_file)
			self.BuildIndex(header_info,dna)

	# load fmi from encoded file
	def loadFMI(self, index_id):
		fmi_loc = getFMIFile(self.fasta_dir, index_id)
		file = open(fmi_loc, 'rb')
		data = pickle.load(file)
		return data

	def setIndexedGnomes(self,inds):
		self.indexed_gnomes = inds

	def AllignExatcly(self, short_read):
		most_likely_gnome_id, freq  = None , None
		for ref_gnome_id in self.indexed_gnomes:
			index = self.loadFMI(ref_gnome_id)
			result = index.query(short_read)

			if most_likely_gnome_id is None:
				most_likely_gnome_id, freq = ref_gnome_id, result
			elif freq < result:
				most_likely_gnome_id, freq = ref_gnome_id, result
		
		if most_likely_gnome_id and freq > 0:
			return most_likely_gnome_id, freq

		else:
			return None, None

	def AllignApproximately(self, short_read):
		pass



if __name__ == '__main__':
	al = Aligner('data/dataset1/')
	#al.BuildIndexes()
	#print(al.loadFMI('aname'))
	#al = Aligner('data/dataset1/')
	al.setIndexedGnomes(['1','2'])
	res = al.AllignExatcly("CAATT")
	print(res)