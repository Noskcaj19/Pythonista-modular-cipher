from cipher import Cipher
from modules import *
from functools import partial
import clipboard
import ui


class main(ui.View):
	def __init__(self, ciphers, width, height):
		self.name = 'Ciphers'
		self.ciphers = ciphers
		self.width = width
		self.height = height
		self.listItems = []
		self.showCiphers = False
		self.decode = False
		self.customItems = []
		cipher = self.ciphers[0]
		try:
			if cipher.needs_view:
				self.cipher = cipher(self)
				for item in self.cipher.makeItems():
					self.add_subview(item)
					self.customItems.append(item)
		except:
			self.cipher = cipher()
		
		self.cipherLabel = ui.Label()
		self.cipherLabel.text = self.ciphers[0].name
		self.cipherLabel.center = (self.width / 4, 25)
		self.cipherLabel.flex = 'RL'
		self.add_subview(self.cipherLabel)
		
		self.modeLabel = ui.Label()
		self.modeLabel.text = 'Encode'
		self.modeLabel.center = (self.width/2, self.height/6.5)
		self.modeLabel.alignment = ui.ALIGN_CENTER
		self.modeLabel.flex = 'RL'
		self.add_subview(self.modeLabel)
		
		self.errorLabel = ui.Label()
		self.errorLabel.text_color = 'red'
		self.errorLabel.width = self.width / 2.2
		self.errorLabel.center = (0, 25)
		self.errorLabel.x = self.width/1.8
		self.add_subview(self.errorLabel)
		
		self.scroll = ui.ScrollView()
		self.scroll.border_width=1
		self.scroll.flex = 'RLTB'
		self.scroll.width = self.width /1.3
		self.scroll.height = self.height/1.3
		self.scroll.center = (self.width/2, self.height/2)
		self.scroll.hidden = True
		self.scroll.background_color = 'white'
		self.scroll.flex = 'RLTWHB'
		self.add_subview(self.scroll)
		
		self.ciphersButton = ui.Button(title='Ciphers')
		self.ciphersButton.center = (self.width/2, 25)
		self.ciphersButton.action = self.toggleCiphers
		self.ciphersButton.flex = 'RL'
		self.add_subview(self.ciphersButton)
		
		self.modeSwitch = ui.Switch()
		self.modeSwitch.action = self.changeMode
		self.modeSwitch.center = (self.width/2, self.height/5)
		self.modeSwitch.flex = 'RL'
		self.add_subview(self.modeSwitch)
		
		self.inBox = ui.TextView(name='in')
		self.inBox.border_width = 1
		self.inBox.x = (self.width/20) - 15
		self.inBox.width = self.width / 2.4
		self.inBox.height = self.height / 1.3
		self.inBox.y = 50
		self.inBox.delegate = self
		self.inBox.flex = 'RBHW'
		self.add_subview(self.inBox)
		
		self.outBox = ui.TextView(name='out')
		self.outBox.delegate = self
		self.outBox.border_width = 1
		self.outBox.x = (self.width/20) + (self.width/2)
		self.outBox.width = self.width / 2.4
		self.outBox.height = self.height / 1.3
		self.outBox.y = 50
		self.outBox.flex = 'LBHW'
		self.add_subview(self.outBox)
		
		self.copyButton = ui.Button(title='Copy')
		self.copyButton.title = 'Copy'
		self.copyButton.center = (self.width/2, (self.height/4)+5)
		self.copyButton.action = self.copy_action
		self.add_subview(self.copyButton)
		
		self.pasteButton = ui.Button(title='Paste')
		self.pasteButton.center = (self.width/2, (self.height/4)+50)
		self.pasteButton.action = self.paste_action
		self.add_subview(self.pasteButton)
		
		self.scroll.bring_to_front()
		
		self.makeItems()

	def makeItems(self):
		if not self.listItems == []:
			for item in self.listItems:
				self.remove_subview(item)
			self.listItems = []
		
		height = 50
		current_y = 0
		for index, item in enumerate(self.ciphers):
			listItem = ui.View()
			listItem.width = self.scroll.width / 2
			listItem.x = (index % 2) * self.scroll.width / 2
			listItem.y = current_y
			if index % 2:
				current_y += height

			listItem.height = height
			
			label=ui.Label()
			label.text = str(item.name)
			label.width = listItem.width - 50
			label.x = 50
			label.height = height
			listItem.add_subview(label)
			
			button = ui.Button(title='')
			button.border_width=1
			button.y = height/5
			button.x = 10
			button.corner_radius = 10
			button.cipher = self.ciphers[index]
			button.action = partial(self.setCipher, button.cipher)
			button.background_color = 'blue'
			
			listItem.add_subview(button)
			#listItem.cipher = ciphers[index]
			
			self.scroll.add_subview(listItem)
			self.listItems.append(listItem)

		# '-1' fixes side swiping
		self.scroll.content_size = (self.scroll.width-1, len(self.listItems)*height)
	
	def setCipher(self, cipher, sender):
		for item in reversed(self.customItems):
			view.remove_subview(item)
		self.customItems = []
		
		try:
			if cipher.needs_view:
				self.cipher = cipher(self)
				for item in self.cipher.makeItems():
					self.add_subview(item)
					self.customItems.append(item)
		except:
			self.cipher = cipher()
			
		self.cipherLabel.text = cipher.name
		self.toggleCiphers(None)
		self.textview_did_change(self.inBox)
		self.textview_did_change(self.outBox)
		
	def changeMode(self, sender):
		if sender.value:
			self.decode = True
			self.modeLabel.text = 'Decode'
		else:
			self.decode = False
			self.modeLabel.text = 'Encode'
		self.textview_did_change(self.inBox)
		self.textview_did_change(self.outBox)

	def toggleCiphers(self, sender):
		# Dismiss keyboard
		self.inBox.editable = False
		self.inBox.editable = True
		self.outBox.editable = False
		self.outBox.editable = True

		# Toggle Visibility
		if self.showCiphers:
			self.scroll.hidden = True
			self.showCiphers = False
		else:
			self.scroll.hidden = False
			self.showCiphers = True

	def textview_did_change(self, textview):
		try:
			self.errorLabel.text = ''
			if textview.name == 'in' and not self.decode:
				self.outBox.text = str(self.cipher.encode_text(textview.text))
			if textview.name == 'out' and self.decode:
				self.inBox.text = str(self.cipher.decode_text(textview.text))
		except Exception as e:

			if len(e.args) == 1:
				self.errorLabel.text = str(e.args[0])
			else:
				self.errorLabel.text = str(e.args[0]) + ' ' + str(e.args[-1])

	def copy_action(self, sender):
		if self.decode:
			clipboard.set(str(self.inBox.text))
		else:
			clipboard.set(str(self.outBox.text))

	def paste_action(self, sender):
		if self.decode:
			self.outBox.text = str(clipboard.get())
		else:
			self.inBox.text = str(clipboard.get())

ciphers = Cipher.__class__.__subclasses__(Cipher)
ciphers = sorted(ciphers, key=lambda x: x.name)

width, height = ui.get_screen_size()
view = main(ciphers, width, height)
view.present('panel')
