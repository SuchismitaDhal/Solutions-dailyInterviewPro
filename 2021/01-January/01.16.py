# GOOGLE
"""
	SOLVED -- GEEKS FOR GEEKS | Convert nested dictionary into flattened dictionary
	Given a nested dictionary, flatten the dictionary, where nested dictionary 
	keys can be represented through dot notation.
	Example:
		Input: {
			'a': 1,
			'b': {
				'c': 2,
				'd': {
					'e': 3
				}
			}
		}
		Output: {
			'a': 1,
			'b.c': 2,
			'b.d.e': 3
		}
	You can assume there will be no arrays, and all keys will be strings.
"""

def flatten_dictionary(d):
	# Time: O(n) 	Space: O(h)
	sol = dict()
	for key, value in d.items():
		if type(value) == dict:
			for k, v in flatten_dictionary(value).items():
				sol[key+ '.' + k] = v
		else:
			sol[key] = value
	return sol

d = {
	'a': 1,
	'b': {
		'c': 2,
		'd': {
			'e': 3
		}
	}
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
