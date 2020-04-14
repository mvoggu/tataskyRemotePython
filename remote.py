import socket

hostIP = '192.168.0.6'

class Tatasky:
	
	buttonPower = 'e0 00'
	buttonSelect = 'e0 01'
	buttonBack = 'e0 02'
	buttonVolumeUp = 'e0 03'
	buttonVolumeDown = 'e0 04'
	buttonMute = 'e0 05'
	buttonChannelUp = 'e0 06'
	buttonChannelDown = 'e0 07'
	buttonApps = 'e0 08'
	buttonHelp = 'e0 09'
	buttonSettings = 'e0 0a'
	buttonGuide = 'e0 0b'
	buttonInfo = 'e0 0e'
	buttonHome = 'e0 10'
	buttonUp = 'e1 00'
	buttonDown = 'e1 01'
	buttonLeft = 'e1 02'
	buttonRight = 'e1 03'
	buttonRed = 'e2 00'
	buttonGreen = 'e2 01'
	buttonYellow = 'e2 02'
	buttonBlue = 'e2 03'
	button0 = 'e3 00'
	button1 = 'e3 01'
	button2 = 'e3 02'
	button3 = 'e3 03'
	button4 = 'e3 04'
	button5 = 'e3 05'
	button6 = 'e3 06'
	button7 = 'e3 07'
	button8 = 'e3 08'
	button9 = 'e3 09'
	buttonPlay = 'e4 00'
	buttonPause = 'e4 01'
	buttonRecord = 'e4 03'
	buttonForward = 'e4 04'
	buttonRewind = 'e4 06'
	buttonTV = 'ef 00'
	buttonFavs = 'ef 01'
	buttonPlan = 'ef 02'
	buttonOnDemand = 'ef 03'

	def __init__(self, p_hostIP, p_hostPORT = 5900):
		self.ip = p_hostIP
		self.port = p_hostPORT

		self.socket = self.__createSocket()

	def click(self, button):
		self.socket.send(bytes.fromhex(f'04 01 00 00 00 00 {button} 04 00 00 00 00 00 {button}'))


	def __createSocket(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip, self.port))

		assert s.recv(50) == b'RFB 003.008\n', "Incorrect Init data from remote. Should be RFB 003.008\n"
		s.send(bytes('RFB 003.008\n', 'ascii'))

		assert s.recv(50) == bytes.fromhex('01 01')
		s.send(bytes.fromhex('01'))

		_ =  s.recv(50)
		s.send(bytes.fromhex('01'))

		_ = s.recv(50)

		return s
	
	def __del__(self):
		self.socket.close()


if __name__ == '__main__':

	t = Tatasky(hostIP)
	t.click(Tatasky.buttonSelect)