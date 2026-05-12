a = 1
S = 0

for i in range(1, 40, 2):
    S += i/a
    a = a*2
print(f"{S:.2f}")
