matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        n = float(input())
        linha.append(n)
    matriz.append(linha)
print("Elementos fora da diagonal principal:")
for i in range(10):
    for j in range(10):
        if i != j:
            print(matriz[i][j])

print("Elementos abaixo da diagonal principal::")
for i in range(10):
    for j in range(10):
        if i > j:
            print(matriz[i][j])

print("A soma de cada linha da matriz é:")

for i in range(10):
    soma = 0
    for j in range(10):
        soma += matriz[i][j]
    print(soma)

print("Produto de cada coluna:")
for j in range(10):
    produto = 1

    for i in range(10):
        produto *= matriz[i][j]

    print(produto)
