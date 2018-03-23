
#christopher taylor 07/03/18 using code from Ben Knisley found at: https://gist.github.com/BenKnisley/5647884
import socket, time
import diffiehellmanv2_live as dh

public,a = dh.get_publickey()

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return
   
def Tcp_Write(D):
    temp_s = (D + '\r')
    s.send(temp_s.encode('utf-8'))
    return 
   
def Tcp_Read():
	a = ' '
	b = ''
	while a != '\r':
		a = bytes.decode(s.recv(1))
		b = b + a
	return b

def Tcp_Close( ):
   s.close() 
   

Tcp_connect( '192.168.0.19', 17098)
Tcp_Write(str(public))
readData = int(Tcp_Read())
print("Public", public)
print("read data", readData)
shared = dh.get_sharedkey(a, int(readData))
#Tcp_Write(str(shared))
print("shared", shared)
print('closing connection')
Tcp_Close()
print('connection closed')

#import sys
#from socket import socket, AF_INET, SOCK_DGRAM
#
#SERVER_IP   = 
#PORT_NUMBER = 5000
#SIZE = 1024
#
#import time
#import diffiehellmanv2_live as dh
#
#secret = 0
#recieved = False
#mySocket = socket( AF_INET, SOCK_DGRAM )
#mySocket.connect((SERVER_IP,PORT_NUMBER))
#myMessage = dh.get_publickey()
#
#mySocket.send(str(myMessage).encode('utf-8'))
#mySocket.close()
#mySocket.connect((SERVER_IP,PORT_NUMBER))
#while recieved == False:
#
#(data,addr) = mySocket.recv(SIZE)
#secret = dh.get_sharedkey(int(data))
#print(secret)
#print(data)
#mySocket.close()    
#
#mySocket.sendto(myMessage1.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
#
#sys.exit()

#!/usr/bin/env python
