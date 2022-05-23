# EXAMPLE OF NESTED CLASS
class collage:
    def __init__(self):
        print("construct or is called")
    def year(self):
        print("year is 2021")

    #STARTING OF NESTED CLASS
    
    class student:
        def __init__(self, name, roll_no):
            self.name = name
            self.roll = roll_no
        def info(self):
            print(f"student name is{self.name}and age is{self.roll}")
            
stu = collage()
stu.year()
p = stu.student("Ankush", 21)
print(p.name)

