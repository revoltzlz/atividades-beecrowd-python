import random
v1 = []
v2 = []
for i in range(75):
    v1.append(random.randint(-1000, 1000))
    v2.append(random.randint(-1000, 1000))
v3 = []
for i in range(75):
    v3.append(v1[i]+v2[i])
