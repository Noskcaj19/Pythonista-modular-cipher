from cipher import Cipher
import string
from itertools import product


class sequnce(Cipher):
	name = 'Sequence'
	def __init__(self):
		all_chars = '0123456789'
		sequences = [''.join(sequence) for sequence in product(all_chars, repeat=2)]
		self.u_a = {key:value for key, value in zip(sequences, string.printable)}
		self.a_u = {value:key for key,value in self.u_a.items()}

	def encode_text(self, i: str) -> str:
		x = [self.a_u[x] for x in i]
		return ''.join(x)

	def decode_text(self, i: str) -> str:
		if len(i) == 0 or len(i) % 2 != 0:return 
		x = []
		for ind in range(0, len(i)-1, 2):
			k = i[ind] + i[ind+1]
			x.append(self.u_a[k])
		return ''.join(x)
