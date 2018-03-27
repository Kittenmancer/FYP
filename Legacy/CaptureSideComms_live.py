#Capture
import socket
import io, base64
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destination = 192.168.0.2		    #This is the servers TCP/IP address.
port = 17098 									#Port of your choice (NOT 80)
bufferSize = 20000000
handshake = str.encode('Whatever')       #This could be your public key maybe?

#sentFile = open('small.png', 'rb')
sentFile = open('/home/pi/Desktop/CameraCapture.jpg', 'rb')

byteStream = base64.b64encode(sentFile.read())

sock.connect((destination, port))
sock.send(handshake)
data = sock.recv(bufferSize)
if (data):
	sock.sendall(byteStream)
	response = sock.recv(bufferSize)
	if (response == 'True'):
		sock.close()
		#connectionOpen = False
		#break
