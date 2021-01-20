# FACEBOOK
"""
	SOLVED -- GEEKS FOR GEEKS | Find shortest unique prefix for every word in a given list | Set 1 (Using Trie)
	Given a list of words, for each word find the shortest unique prefix. 
	You can assume a word will not be a substring of another word 
	(ie play and playing won't be in the same words list)
	Example
		Input: ['joma', 'john', 'jack', 'techlead']
		Output: ['jom', 'joh', 'ja', 't']
"""
class TrieNode:
	def __init__(self, val):
		self.val = val
		self.children = []

	def insert(self, word):
		if not word: return

		c = word[0]
		for child in self.children:
			if child.val == c:
				child.insert(word[1:])
				return

		newchild = TrieNode(c)
		self.children.append(newchild)
		newchild.insert(word[1:])

	def get_substrings(self):
		if not self.children: return ['']
		sol = []
		for child in self.children:
			subs = child.get_substrings()
			for s in subs:
				sol.append(child.val + s)
		return sol

	def __str__(self):
		for child in self.children:
			print(child)
		return self.val + '(' + ', '.join([c.val for c in self.children]) + ')'

def delete_linear_branch(trie):
	factor = 0
	for child in trie.children:
		factor += max(delete_linear_branch(child), 1)

	if factor == 1: trie.children = []
	return factor

def shortest_unique_prefix(words):
	# Time: O(nm)		Space: O(nm)
	# n: number or words		m: number of letters in word
	if len(words) == 0: return []
	if len(words) == 1: return [words[0]]

	trie = TrieNode('.')
	for word in words:
		trie.insert(word)

	delete_linear_branch(trie)
	return trie.get_substrings()

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
