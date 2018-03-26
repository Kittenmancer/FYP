import socket, base64
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname() #as we're locally hosted, this is the same IP as the server.
port = 17098
bufferSize = 9999999
handshake = str.encode('Hi')

socketConnection.connect((IP, port))
socketConnection.send(handshake)
data = socketConnection.recv(bufferSize)
byteString = base64.b64decode(data)
with open("imageToSave.png", "wb") as fh:
   fh.write(base64.decodebytes(data))
socketConnection.close()
