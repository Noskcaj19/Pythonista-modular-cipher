#!python2
from cipher import Cipher

class rot47(Cipher):
	name = 'Rot47'
	def encode_text(self, plain_text: str) -> str:
		x = []
		for i in range(len(plain_text)):
			j = ord(plain_text[i])
			if j >= 33 and j <= 126:
				x.append(chr(33 + ((j + 14) % 94)))
			else:
				x.append(plain_text[i])
		a = ''.join(x)
		return a
	
	def decode_text(self, cipher_text: str) -> str:
		x = []
		for i in range(len(cipher_text)):
			j = ord(cipher_text[i])
			if j >= 33 and j <= 126:
				x.append(chr(33 + ((j + 14) % 94)))
			else:
				x.append(cipher_text[i])
		a = ''.join(x)
		return a

