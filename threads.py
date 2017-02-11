import threading
import time


def myFunc():
    print("start", threading.currentThread().name)
    time.sleep(3)
    print("End", threading.currentThread().name)


threads = []
for i in range(5):
    # initialize a thread with a name and target function
    th = threading.Thread(target=myFunc, name="thread" + str(i))
    th.start()
    threads.append(th)

for i in threads:
    i.join()  # waits for all the thread to complete before proceeding

print("kp")
