from multiprocessing.connection import Client
c = Client(('127.0.0.1', 25000), authkey=b'peekaboo')
c.send('hello')
c.recv()
c.send(42)
c.recv()
c.send([1, 2, 3, 4, 5])
c.recv()

