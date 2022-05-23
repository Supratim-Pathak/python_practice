
from threading import Thread, current_thread

def tTestung(a):
    print("thread is running", current_thread())
    current_thread().name = "Test Thread_1"
    print("thread is running", current_thread())

t = Thread(target=tTestung, args=(12,))
t.start()

for i in range(5):
    current_thread().setName("jsdfsa")
    print(i, current_thread().getName())

