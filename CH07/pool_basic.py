import multiprocessing as mp

def test():
    pass

p = mp.Pool()

for i in range(10):
    p.apply_async(test) 

p.close() 
p.join()
