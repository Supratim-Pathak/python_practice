class father:
    money = 1000 

    @classmethod
    def income(cls):
        print(f"Father income is{cls.money}")

class son(father):
    def sonIncome():
        print("son name is Suraj")

obj  =  son()
obj.income()


