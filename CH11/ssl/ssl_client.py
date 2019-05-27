from socket import socket, SOCK_STREAM, AF_INET
import ssl

s = socket(family= AF_INET, type=SOCK_STREAM)
s_ssl = ssl.wrap_socket(s,
                        cert_reqs = ssl.CERT_REQUIRED,
                        ca_certs = 'server_cert.pem'
                        )
s_ssl.connect(('127.0.0.1',10000))
s_ssl.send(b'Hello, World!')
data = s_ssl.recv(1024)
print('data recv:', data)

