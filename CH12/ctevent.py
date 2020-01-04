from threading import Event, Thread
import time

def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

started_evt = Event()

print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t1 = Thread(target=countdown, args=(20, started_evt))
t.start()
t1.start()
started_evt.wait()
print('countdown is running')
print('countdown is running 2')
