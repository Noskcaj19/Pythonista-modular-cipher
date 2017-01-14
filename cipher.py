class Cipher (object):
	""" Class Structure for all subclasses
	"""
	def __init__(self):
		pass
	
	def encode_text(self, plain_text: str) -> str:
		pass
	
	def decode_text(self, cipher_text: str) -> str:
		pass
	
	def __str__(self):
		return self.name
