#!/usr/bin/env python3

import threading

a = 0

def f1():
    global a
    for i in range(10_000_000):
        #a = a + 1
        a += 1

def f2():
    global a
    for i in range(10_000_000):
        a -= 1

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()

print(a)
