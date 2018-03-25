import socket
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
socketConnection = socket.gethostname()
host = socket.gethostname()
port = 17099
socketConnection.connect((host, port))
newFile = open('CapturedImage'+timestr+'.png')
print('Incoming transmission')
l = socketConnection.recv(1024)
while(l):
    print('Recieving transmission...')
    newFile.write(l)
    l=socketConnection.recv(1024)
newFile.close()
print('Transmission received')
socketConnection.shutdown(socket.SHUT_WR)
soccketConenction.close
