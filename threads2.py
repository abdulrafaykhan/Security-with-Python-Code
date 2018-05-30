import threading
import time

class aThread(threading.Thread):
    def __init__(self, num, val, count):
        threading.Thread.__init__(self)
        self.numThread = num
        self.valThread = val
        self.loopcount = count

    def run(self):
        print("Starting to run...")
        print("Thread No. ", self.numThread)
        myfunc(self.numThread, self.valThread, self.loopcount)

def myfunc(num, val, count):
    sum = 0
    for i in range(1, count):
        if (sum != 0):
            sum = num * val
        else:
            sum = sum + num * val
        time.sleep(0.3)
    print("The answer is ", sum)

t1 = aThread(1, 4, 2)
t2 = aThread(2, 4, 2)
t3 = aThread(3, 4, 3)
t4 = aThread(4, 4, 4)
t5 = aThread(5, 4, 5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
threads.append(t5)

for t in threads:
    t.join()