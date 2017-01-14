from cipher import Cipher
from ui import Label

class legnth (Cipher):
	""" Parent view interaction demo
	"""
	name = 'Length'
	needs_view = True
	view = None
	customItems = []

	def __init__(self, view):
		self.view = view
	
	def makeItems(self):
		self.customItems = []

		self.out_length_label = Label()
		self.out_length_label.text = ''
		self.out_length_label.center = ((self.view.width/3)+(self.view.width/2), 25)
		self.customItems.append(self.out_length_label)
		
		self.in_length_label = Label()
		self.in_length_label.text = ''
		self.in_length_label.center = ((self.view.width/3)+20, 25)
		self.customItems.append(self.in_length_label)
		
		return self.customItems
	
	
	# Does not do a text manipulation, just provieds a text length label
	def encode_text(self, plain_text: str) -> str:
		return plain_text
		
	def decode_text(self, cipher_text: str) -> str:
		return cipher_text
