matriz = []
notas = []
for i in range(10):
    linha = []
    for j in range(5):
        n = float(input())
        linha.append(n)
    matriz.append(linha)
maior_soma = 0
melhor_atleta = 0

for i in range(10):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    if soma > maior_soma:
        maior_soma = soma
        melhor_atleta = i
