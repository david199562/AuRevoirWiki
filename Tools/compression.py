# "There should be no such thing as boring mathematics." - Edsger Dijkstra

'''
Huffman
'''
class HuffmanNode():
	count = 0
	char = ''
	c0 = ''
	c1 = ''
	p = ''
	
	def __init__(self, count, char, c0, c1, p):
		self.count, self.char, self.c0, self.c1, self.p = count, char, c0, c1, p
	
	def __lt__(self, other):
		if self.count != other.count:
			return self.count > other.count# reverse since minheap
		# if there is a tie, consider the ascii value 
		return self.char > other.char# reverse since only minheap provided

class HuffmanTree():
	
	root = 0
	leaves = []
	
	def __init__(self):
		self.root = 0
		
		#initialize the leave list with 256 ascii value
		self.leaves = [None]*256

	def build(self,freq):
	
		freq.sort()
		pri_q = []
		
		#put all element in priority queue
		for e in freq:
			if e.count:
				heappush(h, e)
		
		#construct tree
		while pri_q:
			node = HuffmanNode()
			
	def encode(self):
		pass
	
	def decode(self):
		pass

def compress(src_str):
	#get the freq vector first    
	
	return 


def decompress(pickle):
    return cucumber
