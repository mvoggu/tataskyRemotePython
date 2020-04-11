import socket

hostIP = '192.168.0.6'

class Tatasky:
	
	buttonMute = bytes.fromhex('04 01 00 00 00 00 e0 05 04 00 00 00 00 00 e0 05')
	buttonSelect = bytes.fromhex('04 01 00 00 00 00 e0 01 04 00 00 00 00 00 e0 01')

	def __init__(self, p_hostIP, p_hostPORT = 5900):
		self.ip = p_hostIP
		self.port = p_hostPORT

		self.socket = self.__createSocket()

	def click(self, button):
		self.socket.send(button)


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
	t.click(Tatasky.buttonMute)