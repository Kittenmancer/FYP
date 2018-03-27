#RECEIVER
#!/usr/bin/env python
import socket, time
import diffiehellmanv2_live as dh
from AESCrypto_live import AESCipher
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


Tcp_server_wait ( 50, 17098 )
Tcp_server_next()
Tcp_Write(str(public))
readData = int(Tcp_Read())
#print("Public", public)
#print("read data", readData)
my_prime, my_key = dh.get_sharedkey(a, int(readData))
my_cipher = AESCipher(my_key)
#print("shared",shared)
#image = Tcp_Read()
#fp = open("imageToSave.png",'wb')
recievedString = s.recv(20000000)
decryptedString = my_cipher.decrypt(recievedString)
#fp.write(image.encode())
print("Encrypted data received over network: ", recievedString)
print("Decrypted Data: ", decryptedString)
#while True:
#    data= s.recv(1024)
#    if not data:
#        break
#    fp.write(data)
#fp.close()
print('closing connection')
Tcp_Close()
print('connection closed')
