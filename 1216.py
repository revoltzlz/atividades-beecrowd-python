soma = 0
quantidade = 0

while True:
    try:
        nome = input()
        distancia = int(input())
        quantidade += 1
        soma += distancia
        media = soma/quantidade
    except:
        break
print(f"{media:.1f}")
