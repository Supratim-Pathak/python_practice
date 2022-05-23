from abc import ABC, abstractmethod

class father(ABC):
    def __init__(self, *args):
        super(father, self).__init__(*args)

    @abstractmethod
    def add(self, a, b):
        pass
    
    def show(self):
        print("This is concrete Method")

class subCls(father): 
    def add(self, a, b):
        print(f"This is concrete Method{a+b}")

obj =  subCls()
obj.add(120,122)