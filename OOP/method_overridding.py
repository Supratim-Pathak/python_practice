class add():
    def result(self, x, y):
        print('Addition:', x+y)

class multi(add):
    def result(self, x, y):
        # SUPER IS USED TO ACESS METHOD FROM PARENT CLASS HAVING SAME NAME
        super().result(10,10)
        print('Multi:', x*y)

c = multi() 
c.result(12, 16)
        
        
        
        
    
        