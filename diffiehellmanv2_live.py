# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function
import random
import numpy as np
import os
from binascii imprt unhexlify, hexlify
import hashlib
from hkdf import Hkdf

sharedPrime = 0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371
sharedBase = 2

def get_publickey():
    a = int.from_bytes(os.urandom(64), byteorder='big')
     # a
# Alice Sends Bob A = g^a mod p
    return pow(sharedBase,a,sharedPrime), a

def get_sharedkey(a, B):
# Alice Computes Shared Secret: s = B^a mod p

    x = pow(B,a,sharedPrime)
    aKDF = Hkdf(none, str(x).encode(), hash=hashlib.sha512)
    #print(x)
    return x, aKDF

