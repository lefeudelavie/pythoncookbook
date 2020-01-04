from threading import Thread
from queue import Queue

_sentinel = object()


def procuder(out_q):
    while running:
        # procude data
        ....
        out_q.put(data)
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()

        if data is _sentinel:
            in_q.put(_sentinel)
            break
