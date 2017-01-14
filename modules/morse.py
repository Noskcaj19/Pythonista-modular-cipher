# coding: utf-8
from cipher import Cipher


class morseCode(Cipher):
	name = 'Morse'
	def __init__(self):
		self.morse_encoding_map = {
			"A": ".-", "B": "-...",
			"C": "-.-.", "D": "-..",
			"E": ".", "F": "..-.",
			"G": "--.", "H": "....",
			"I": "..", "J": ".---",
			"K": "-.-", "L": ".-..",
			"M": "--", "N": "-.",
			"O": "---", "P": ".--.",
			"Q": "--.-", "R": ".-.",
			"S": "...", "T": "-",
			"U": "..-", "V": "...-",
			"W": ".--", "X": "-..-",
			"Y": "-.--", "Z": "--..",
			"0": "-----", "1": ".----",
			"2": "..---", "3": "...--",
			"4": "....-", "5": ".....",
			"6": "-....", "7": "--...",
			"8": "---..", "9": "----.",
			".": ".-.-.-", ",": "--..--",
			":": "---...", ";": "-.-.-.",
			"?": "..--..", "-": "-...-",
			"_": "..--.-", "(": "-.--.",
			")": "-.--.-", "'": ".----.",
			"=": "-...-", "+": ".-.-.",
			"/": "-..-.", "@": ".--.-.",
			"$": "...-..-", "!": "-.-.--"
		}
		self.morse_decoding_map = {value:key for key,value in self.morse_encoding_map.items()}

	def encode_text(self, plain_text: str) -> str:
		unusable_chars = "\"#%&*<>[\]^`{|}~"
		morsestring = []
	
		for i in unusable_chars:
			plain_text = plain_text.replace(i, "")
		plain_text = plain_text.upper()
	
		words = plain_text.split(" ")
		for word in words:
			letters = list(word)
			morse_word = []
			for letter in letters:
				morse_letter = self.morse_encoding_map[letter]
				morse_word.append(morse_letter)
			word = "|".join(morse_word)
			morsestring.append(word)
		return "||".join(morsestring)
	
	def decode_text(self, cipher_text: str) -> str:
		characterstring = []
		if cipher_text[-1] == "|" and cipher_text[-2] == "|":
			cipher_text = cipher_text[:-2]
		if cipher_text[-1] == "|":
			cipher_text = cipher_text[:-1]
		words = cipher_text.split("||")
		for word in words:
			letters = word.split("|")
			characterword = []
			for letter in letters:
				try:
					characterletter = self.morse_decoding_map[letter]
					characterword.append(characterletter)
				except KeyError:
					pass
			word = "".join(characterword)
			characterstring.append(word)
		return " ".join(characterstring)
