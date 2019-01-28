import multiprocessing, time, signal

def fu():
    time.sleep(1)
    print 'fu'

def pr():
    print 'print'
    
def fun():
    p = multiprocessing.Process(target=fu)
    p1 = multiprocessing.Process(target=pr)
    i=1
    #while True:
    print p, p.is_alive()
    print i
    p.start()
    p1.start()
    print p, p.is_alive()
    i=i+1
    p.terminate()
    p1.terminate()
    time.sleep(0.1)
    print p, p.is_alive()
    p.exitcode == -signal.SIGTERM
    #    if i==10:
    #        break

j=1
while True:
    j=j+1
    fun()
    if j==10:
        break
