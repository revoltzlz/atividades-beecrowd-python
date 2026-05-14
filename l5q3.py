v = []
for i in range(15):
    n = float(input())
    v.append(n)
maior = max(v)
menor = min(v)

for i in range(15):
    if v[i] == maior:
        print(f"O maior valor é {v[i]} e esta na posição {i}")
    if v[i] == menor:
        print(f"O menor valor é {v[i]} e esta na posição {i}")
