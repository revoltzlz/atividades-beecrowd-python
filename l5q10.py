import random

v = []

for i in range(1000):
    v.append(random.randint(1, 100))

n = float(input())
soma = 0
for i in range(1000):
    if v[i] == n:
        soma += 1
print(soma)
