#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Course Project
#


from util import *
from fmi import *
import pickle
from settings import settings, datasets


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

	def AlignExatcly(self, short_read):
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

	def AlignApproximately(self, short_read):
		matching_threshold = settings['matching_threshold'] #len(short_read)/5
		most_likely_gnome_id, freq, matches  = None , None, None
		for ref_gnome_id in self.indexed_gnomes:
			index = self.loadFMI(ref_gnome_id)
			this_freq, this_matches = index.random_pseudo_align(short_read)

			if (this_matches > matching_threshold) and ((most_likely_gnome_id is None) or (freq < this_freq) or (freq == this_freq and matches < this_matches)):
				most_likely_gnome_id, freq, matches = ref_gnome_id, this_freq, this_matches
				if this_matches > 2*matching_threshold:
					return most_likely_gnome_id, freq, matches



		if most_likely_gnome_id and matches > 0:
			return most_likely_gnome_id, freq, matches

		else:
			return None, None, None



if __name__ == '__main__':
	al = Aligner('data/dataset1/')
	#al.BuildIndexes()
	#print(al.loadFMI('aname'))
	#al = Aligner('data/dataset1/')
	al.setIndexedGnomes(['1','2'])
	res = al.AlignExatcly("CAATT")
	print(res)