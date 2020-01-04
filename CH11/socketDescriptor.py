import multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
import socket


def worker(in_p, out_p):
    out_p.close()
    while True:
        fd = recv_handle(in_p)
        print("CHILD GOT FD", fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno = fd) as s:
            data = s.recv( 8192 )
            if not data:
                break
            print("CHILD RECV:{!r} ".format(data))
            s.send(data)

def server(address, in_p, out_p, worker_pid):
    in_p.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind( address )
    s.listen(1)
    while True:
        c, a = s.accept()
        print("GOT CONNECTION FROM:", a)
        send_handle(out_p, c.fileno(), worker_pid)
        c.close()

if __name__ == '__main__':
    c1, c2 = multiprocessing.Pipe()
    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(target=server, args=(
                                       ("", 10000), c1, c2, worker_p.pid))
    server_p.start()
    c1.close()
    c2.close()




