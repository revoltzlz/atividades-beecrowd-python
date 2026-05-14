import random
matriz = []
for i in range(5):
    linha = []
    for j in range(25):
        linha.append(random.randint(-1000, 1000))
    matriz.append(linha)
print("Primeira coluna:")
for i in range(5):
    print(matriz[i][0])
soma = 0
for i in range(5):
    soma += matriz[i][4]
print("A soma da coluna 5 é:", soma)
