import socket

socketConnection = socket.socket()

host = socket.gethostname()
port = 17099
socketConnection.bind((host, port))
sentFile = open('/home/pi/Desktop/CameraCapture.jpg')
socketConnection.listen(5)

while True:
    client, addr = socketConnection.accept()
    print("connection established from ", addr)
    print("sending file")
    l=sentFile.read(1024)
    while (l):
        print("sending in progress...")
        socketConnection.send(l)
        l=sentFile.read(1024)
    sentFile.close()
    print("File transmission complete")
    socketConnection.close()
