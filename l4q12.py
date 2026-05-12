id = []
preco = []
while True:
    n = int(input())
    if n < 0:
        break
    valor = float(input())
    id.append(n)
    preco.append(valor)

for i in range(len(id)):
    print(f"Id: {id[i]}   -    Valor: {preco[i]:.2f}")

total = sum(preco)
print(f"O valor total do caixa é {total:.2f}")
