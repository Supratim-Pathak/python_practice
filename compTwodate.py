from datetime import date
d1 = date(year=2019, month=9, day=12)
d2 = date(year=2019, month=9, day=11)
print(d1)
print(d2)
if d1==d2:
    print("Equal")
else:
    print("not Equal")