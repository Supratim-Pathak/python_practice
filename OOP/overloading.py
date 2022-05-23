from pyparsing import And


class calculate:
    def sum(self, a=None, b=None, c=None):
        if a==None and b==None and c==None:
            print("No Argument passed")
        elif a==None and b==None:
            print("a & c is not present")
        elif a==None and c==None:
            print("a & c is not present")
        elif c==None and b==None:
            print("a & c is not present")
        else:
            s = a+b+c
            return s

c = calculate()
print(c.sum(12,10))