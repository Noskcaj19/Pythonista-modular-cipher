from cipher import Cipher
from base64 import b64decode, b64encode

class base64(Cipher):
	"""Simple base64 implementation
	"""
	name = 'Base64'
	def encode_text(self, plain_text: str) -> str:
		return b64encode(plain_text.encode()).decode()

	def decode_text(self, cipher_text: str) -> str:
		return b64decode(cipher_text.encode()).decode()
