from concurrent.futures import thread
# from threading import Thread ,current_thread
from threading import *

def disp():
    print("This is child thread !!!", current_thread())
    # current_thread().name = 'test-1'
    current_thread().setName('test-1')
    print("This is child thread !!!", current_thread())

# CALLING THE THREAD

t= Thread(target=disp)
t.start()
print("This is Main thread !!!", current_thread().getName())
print(current_thread().getName())