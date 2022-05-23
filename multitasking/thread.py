from threading import Thread
def disp():
    for i in range(5):
        print("This is child thread",)

t =  Thread(target=disp)
t.start()

for i in range(5):
        print("This is Main thread") 