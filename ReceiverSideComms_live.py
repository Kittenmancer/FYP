#Receiver
import socket
import io, base64
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()		    #This is the servers TCP/IP address.
port = 17098 									#Port of your choice (NOT 80)
bufferSize = 20000000
handshake = str.encode('serverPublicKey') 	#Put the server key here
print (host)									#Now we know what the client has to connect to!

sock.bind((host, port))
sock.listen(5)

client, address = sock.accept()
print ('Connection from:', address)
connectionOpen = True

while connectionOpen:
	clientKey = client.recv(bufferSize)
	if not (clientKey): break
	client.sendall(handshake)
	imageData = client.recv(bufferSize)
	print(len(imageData))
	byteStream = base64.b64decode(imageData)
	with open('ImageName.png', 'wb') as fh:
		fh.write(base64.decodebytes(imageData))
	client.send(str.encode('True'))
connectionOpen = False
