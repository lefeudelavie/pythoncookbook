import hmac
from socket import socket, AF_INET, SOCK_STREAM

def client_authenticate(connection, secret_key):
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)

if __name__ == "__main__":
    secret_key = b'abc123'
    s = socket(family= AF_INET, type= SOCK_STREAM)
    s.connect(('localhost', 18000))
    client_authenticate(s, secret_key)
    s.send(b'Hello, world')
    response = s.recv(1024)
    print("Recv response:", response)
