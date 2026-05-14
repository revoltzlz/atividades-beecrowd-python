import random
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randint(-1000, 1000))
    matriz.append(linha)

for i in range(10):
    aux = matriz[1][i]

    matriz[1][i] = matriz[i][7]

    matriz[i][7] = aux

# imprimindo matriz
for i in range(10):
    print(matriz[i])
