nomes = []
precosdol = []
total = []

comprastotais = int(input())

for i in range(comprastotais):
    n = str(input())
    nomes.append(n)
    p = float(input())
    precosdol.append(p)
    t = int(input())
    total.append(t)
print("Relação total de compras:\n")
for i in range(comprastotais):
    total_dolar = precosdol[i]*total[i]
    total_reais = total_dolar*5.65
    print(f"Nome: {nomes[i]}")
    print(f"Preço total em dolar: {total_dolar:.2f}")
    print(f"Preço total em reais: {total_reais:.2f}")
