import random
matriz = []
for i in range(15):
    linha = []
    for j in range(15):
        linha.append(random.randint(-1000, 1000))
    matriz.append(linha)
for i in range(15):
    for j in range(15):
        print(matriz[i][j], end=" ")
    print()
