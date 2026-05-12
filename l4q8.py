v1 = []
v2 = []
for i in range(5):
    n = float(input())
    v1.append(n)
for i in range(5):
    v = float(input())
    v2.append(v)
v3 = []
for i in range(5):
    v3.append(v1[i] + v2[i])
for valor in v3:
    print(valor)
