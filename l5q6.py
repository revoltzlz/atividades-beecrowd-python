import random

v = []

for i in range(100):
    v.append(random.randint(1, 10))

n = int(input())

if n in v:
    print("Esse valor existe!")
else:
    print("Esse valor não existe")
