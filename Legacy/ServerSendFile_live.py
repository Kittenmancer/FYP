import socket
import io, base64
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 17098
bufferSize = 9999999
sentFile = open('small.png','rb')
sentFile = open('/home/pi/Desktop/CameraCapture.jpg', 'rb')
byteString = base64.b64encode(sentFile.read())
with open("manglecheck.png", "wb") as fh:
   fh.write(base64.decodebytes(byteString))
socketConnection.bind((host, port))
socketConnection.listen(5)

client, address = socketConnection.accept()
print ('Connection from:', address)
connectionOpen = True
while connectionOpen:
	data = client.recv(bufferSize)
	if not data: break
	print ("received:", data)
	client.sendall(byteString)
