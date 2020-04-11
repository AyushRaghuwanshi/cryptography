import socket


def nummssg(mssg):
    num_mssg = ''
    for i in mssg:
        if(i == " "):
            num_mssg = num_mssg + '26'
            continue
        i = ord(i.lower()) - 97
        i = str(i)
        if(len(i) == 1):
            i = '0' + i
        num_mssg += i
    return num_mssg

def encmssg(mssg,public_key):
    mssg = int(mssg)
    mssg = (pow(mssg, public_key[0])) % public_key[1]
    mssg = str(mssg)
    return mssg





HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        #taking public key
        public_key = []
        data = conn.recv(1024)
        public_key.append(int(data.decode()))
        data = conn.recv(1024)
        public_key.append(int(data.decode()))
        print("public_key = {}".format(public_key))
        while True:
            text = input("enter mssg to be send ")
            text = nummssg(text)
            print("mssg agter converting it into num = {}".format(text))
            enc_mssg = encmssg(text,public_key)
            print("mssg after encryption = {}".format(enc_mssg))
            conn.send(enc_mssg.encode())
            
        
    