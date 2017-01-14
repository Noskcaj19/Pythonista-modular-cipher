from cipher import Cipher
from modules import *


# Start the encoding or decoding
# This is a simple example and can be replaced with any front-end easily 
ciphers = Cipher.__class__.__subclasses__(Cipher)

print('Listing ciphers...')
for index, cipher in enumerate(ciphers, start=1):
	print('#{}. {}'.format(index, cipher.name))
cipher_choice = input('> ')

try:
	# Initialize the important class
	# Compensate for addition
	cipher = ciphers[int(cipher_choice) - 1]()
except IndexError:
	raise NotImplementedError('Cipher not implemented yet')
except ValueError:
	raise ValueError('Not a number')

print('(Enter nothing for decoding)')
encode_input = input('Encode: ')
if not encode_input == '':
	print(cipher.encode_text(encode_input))
	exit()

decode_input = input('Decode: ')
if not decode_input == '':
	print(cipher.decode_text(decode_input))
