#Capture
#christopher taylor 07/03/18 using code from Ben Knisley found at: https://gist.github.com/BenKnisley/5647884
import socket, time, os
import diffiehellmanv2_live as dh
from AESCrypto_live import AESCipher

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
   

Tcp_connect( '192.168.0.2', 17098)
Tcp_Write(str(public))
readData = int(Tcp_Read())
#print("Public", public)
#print("read data", readData)
my_prime, my_key = dh.get_sharedkey(a, int(readData))
my_cipher = AESCipher(my_key)
#sentFile = open('/home/pi/Desktop/small.png', 'rb')
#byteStream = sentFile.read()
myStringToEncrypt = ("Plain text string example")
byteStream = my_cipher.encrypt(myStringToEncrypt)
print("Original string: ", myStringToEncrypt)
print("Encrypted data sent over network: ", byteStream)
#fp = open("isitworking.png","wb")
#isItWorking = my_cipher.decrypt(byteStream)
#fp.write(isItWorking.encode())
#fp.close()

s.sendall(byteStream)
print('closing connection')
Tcp_Close()
print('connection closed')

