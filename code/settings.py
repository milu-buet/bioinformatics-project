#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Course Project
#

# All the project settings
settings = {
	'gnome_min_length': 50000,
	'gnome_max_length': 100000,
	'read_min_length': 200,
	'read_max_length': 300,
	'error': 0.0,
	'matching_threshold': 8,  # alignapproximately matching
	"reads_sets": {  # read set id: {'coverages': { gnome_id : coverage }}
			1: {   
				'coverages': {
				    1: 1,  
				    2: 2
				}
			},

			2: {
				'coverages': {
				    1: 2,
				    2: 4
				}
			},

			3: {
				'coverages': {
				    1: 3,
				    2: 5
				}
			}

		}

}

#dataset location and number of gnomes
datasets = {
	1: {
		"root": 'data/dataset1/',  #location
		"gnomes": 2, # gnome count
		
	},
	2: {
		"root": 'data/dataset2/',
		"gnomes": 8,
	},
	3: {
		"root": 'data/dataset3/',
		"gnomes": 64,
	}
}
