alturas = []
for i in range(10):
    n = float(input())
    alturas.append(n)
media = sum(alturas) / len(alturas)
for valor in alturas:
    if valor > media:
        print(valor)
