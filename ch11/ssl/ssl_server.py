from socket import socket,SOCK_STREAM,AF_INET
import ssl
import os

KEYFILE  = 'server_key.pem'
CERTFILE = 'server_cert.pem'

def echo_client(s):
    while True:
        data = s.recv(8092)
        if data == b'':
            break
        print("Received mssage:", data.decode())
        s.send(data)
    s.close()
    print("Connection closed")



def echo_server(address):
    s = socket(family= AF_INET, type= SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    
    print('path:', os.getcwd())
    s_ssl = ssl.wrap_socket(s,
                            keyfile = KEYFILE ,
                            certfile = CERTFILE ,
                            server_side = True)
    while True:
        try:
            c, a = s_ssl.accept()
            print('Got a connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}:{}'.format(e.__class__.__name__, e))

echo_server(('127.0.0.1', 10000))


