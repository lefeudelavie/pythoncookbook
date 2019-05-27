import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM

def server_authenticate(connection, secret_key):
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(32)
    return hmac.compare_digest(digest, response)


def echo_handler(client_socket, secret_key):
    if not server_authenticate(client_socket, secret_key):
        client_socket.close()
        return
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            break
        client_socket.sendall(msg)




def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c, b'abc123')

if __name__ == "__main__":
    echo_server(('', 18000))


