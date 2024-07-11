import random

##for n in range(4) :
a1 = random.randrange(10)
a2 = random.randrange(10)
a3 = random.randrange(10)
a4 = random.randrange(10)
while a1 == a2:
    a2 = random.randrange(10)
    if a1 != a2:
        break
while a3 == a2:
    a3 = random.randrange(10)
    if a3 != a2:
        break
while a3 == a1:
    a3 = random.randrange(10)
    if a3 != a1:
        break
while a4 == a1:
     a4 = random.randrange(10)
     if a4 != a3:
        break
while a4 == a2:
    a4 = random.randrange(10)
    if a4 != a3:
        break
while a1 == a3:
    a4 = random.randrange(10)
    if a4 != a3:
        break
print(a1)
print(a2)
print(a3)
print(a4)









