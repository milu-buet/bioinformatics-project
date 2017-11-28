settings = {
	'gnome_min_length': 50000,
	'gnome_max_length': 100000,
	'read_min_length': 200,
	'read_max_length': 300,
	'error': 0.0,
	"reads_sets": {
			1: {   # 1-> read set id
				'coverages': {
				    1: 1,   # gnome_id : coverage
				    2: 2
				}
			},

			2: {
				'coverages': {
				    1: 2,
				    2: 4
				}
			}

		}

}

datasets = {
	1: {
		"root": 'data/dataset1/',
		"gnomes": 2,
		
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
