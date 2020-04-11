import socket
from math import gcd as bltin_gcd

def checkcoprime(p,q):
    return bltin_gcd(p, q) == 1

def numtostr(mssg):
    new_text = ''
    for i in range(int(len(mssg)/2)):
        temp = mssg[i*2:i*2+2]
        if(temp == '26'):
            new_text = new_text + " "
            continue
        temp = int(temp)
        temp = temp + 97
        temp = chr(temp)
        new_text = new_text + temp
    return new_text


def decmssg(mssg, private_key):
    mssg = int(mssg)
    mssg = (pow(mssg, private_key[0])) % private_key[1]
    mssg = str(mssg)
    return mssg

def RSA_Key_Generation():
    p = int(input("select p "))
    q = int(input("select q such that p and q is coprime"))
    while((checkcoprime(p,q)) == False):
        q = int(input("again select q such that p and q is coprime")) 

    n = p*q
    phi = (p-1)*(q-1)
    e = int(input("select e such that "+str(phi)+"and e are coprime"))
    while(checkcoprime(e,phi) == False):
        e = int(input("again select e such that "+str(phi)+"and e are coprime"))

    i = 1
    while(True):
        if((e*i)%phi == 1):
            break
        else:
            i += 1
    
    d = i
    public_key = (e,n)
    private_key = (d,n)

    return (public_key,private_key)




HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    public_key, private_key = RSA_Key_Generation()
    #sending public key to other pc
    s.sendall(str(public_key[0]).encode())
    s.sendall(str(public_key[1]).encode())
    print("public key = {}".format(public_key))
    print("private_key = {}".format(private_key))
    while(True):
        mssg = s.recv(1024)
        mssg = str(mssg.decode())
        print('mssg before decryption = ' + mssg)
        mssg = decmssg(mssg,private_key)
        print("mssg after decryption = {}".format(mssg))
        mssg = numtostr(mssg)
        print("mssg after converting it into char = {}".format(mssg))
        

