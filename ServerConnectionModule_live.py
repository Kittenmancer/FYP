#!/usr/bin/env python
import socket, time
import diffiehellmanv2_live as dh
#things to begin with
#dh.get_publickey()

public,a = dh.get_publickey()

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    print("Socket Open")
    return

def Tcp_server_wait ( numofclientwait, port ):
	global s2
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s2.bind(('',port)) 
	s2.listen(numofclientwait) 

def Tcp_server_next ( ):
		global s
		s = s2.accept()[0]
		print("Connection established")

def Tcp_Write(D):
        temp_s=(D + '\r')
        s.send(temp_s.encode('utf-8'))
        return 

def Tcp_Read( ):
	a = ' '
	b = ''
	while a != '\r':
		a = bytes.decode(s.recv(1))
		b = b + a
	print("handshaking complete")
	return b

def Tcp_Close( ):
   s.close()


Tcp_server_wait ( 5, 17098 )
Tcp_server_next()
#print (Tcp_Read())
Tcp_Write(str(public))
readData = int(Tcp_Read())
print("Public", public)
print("read data", readData)
shared = dh.get_sharedkey(a, int(readData))
print("shared",shared)
#print (Tcp_Read())
print('closing connection')
Tcp_Close()
print('connection closed')
