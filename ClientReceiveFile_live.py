import socket
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
socketConnection=socket.socket()
host = socket.gethostname()
port = 17098
socketConnection.connect((host, port))
newFile = open('CapturedImage'+timestr+'.png', 'wb')
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
