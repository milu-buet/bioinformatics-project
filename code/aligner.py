# Md Lutfar Rahman
#Q4

from util import *
from fmi import *
import pickle

fmi_loc = 'data/fmi/'

class Alligner():
	def __init__(self):
		self.indexed_gnomes = []

	def BuildIndex(self,header,reference_gnome):
		index = FMI(reference_gnome+'$')
		info_dict = self.getHeaderInfo(header)
		#print(info_dict)
		self.indexed_gnomes.append(info_dict['id'])
		#print(">>")
		file = open( fmi_loc + info_dict['id'] + '.pickle', 'wb')
		pickle.dump(index,file)
		return index

	def BuildIndexes(self, dir):
		reference_gnome_files = getFastaFiles(dir)
		for reference_gnome_file in reference_gnome_files:
			header,dna = read_dna_fasta(reference_gnome_file)
			self.BuildIndex(header,dna)

	# load fmi from encoded file
	def loadFMI(self, index_id):
		file = open(fmi_loc + index_id + '.pickle', 'rb')
		data = pickle.load(file)
		return data

	def getHeaderInfo(self,header):
		info_dict = {}
		info_data = header.split('|')
		for data in info_data:
			if ":" in data:
				key,value = data.split(': ')
				info_dict[key] = value
		return info_dict

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
		
		if freq > 0:
			return most_likely_gnome_id, freq

		else:
			return None, None

	def AllignApproximately(self, short_read):
		pass



if __name__ == '__main__':
	#al = Alligner()
	#al.BuildIndexes('data/reference_gnomes/')
	#print(al.loadFMI('aname'))
	al = Alligner()
	al.setIndexedGnomes(['1','2'])
	res = al.AllignExatcly("CAAAAT")
	print(res)