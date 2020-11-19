from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range(10):
            print("I am from thread A")

class B(Thread):
    def run(self):
        for i in range(10):
            print("I am from thread B")

t1 = A()
t2 = B()
t1.start()
t2.start()