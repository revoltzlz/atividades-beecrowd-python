v = []
n = 0
for i in range(50):
    v.append(n)
    n += 1
for i in range(25):
    aux = v[i]
    v[i] = v[49-i]
    v[49-i] = aux
