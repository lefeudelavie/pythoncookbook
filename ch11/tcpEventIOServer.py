import socket
import select

class EventHandler:
    def fileno(self):
        'Return file descriptor'
        raise NotImplemented('Must Implement!')

    def wants_to_send(self):
        'Return Ture if need to send'
        return False

    def handle_send(self):
        'Handle send'
        pass

    def wants_to_receive(self):
        'Return True if need to receive'
        return False

    def handle_recv(self):
        'Handle recv'
        pass


def EventLoop(handlers):
   wants_recv = [h for h in handlers if h.wants_receive()]
   wants_send = [h for h in handlers if h.wants_send()]
   can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
   for h in can_recv:
       h.handle_recv()
   for h in can_send:
       h.handle_send()

class TcpServerHandler(EventHandler):
    def __init__(self, addr, handerlist, client_handler):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSERADDR, True)
        sock.bind(addr)
        sock.listen(1)
        self.sock = sock
        self.handerlist = handlerlist
        self.client_handler = client_handler

    def fileno(self):
        return self.sock.fileno()

    def wants_to_recvive(self):
        return True

    def handle_recv(self):
        client, addr = self.sock.accept()
        self.handlerlist.append(self.client_handler(client,self.handerlist))
    

class TcpClientHandler(EventHandler):
    def __init__(self, sock, hander_list):
        self.sock = sock
        self.hander_list = hander_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]

    def close(self):
        self.sock.close()
        self.hander_list.remove(self)


class TcpEchoClient(TcpClientHandler):
    def wants_to_recv(self):
        return True

    def handle_recv(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


if __name__ == '__main__':
    handerlist = []
    handerlist.append(TcpServerHander(('', 9999),handerlist, TcpEchoClient)
    EventLoop(TcpServerHandler(handerlist))
