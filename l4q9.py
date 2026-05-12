nomes = []
notas = []
for i in range(10):
    n = float(input())
    notas.append(n)
    nome = str(input())
    nomes.append(nome)

maior = max(notas)
menor = min(notas)

for i in range(10):
    if notas[i] == maior:
        print("A maior nota foi do:", nomes[i])
    if notas[i] == menor:
        print("A menor nota foi do:", nomes[i])
