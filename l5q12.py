maiscaro = max(valores)
maisbarato = min(valores)
for i in range(15):
    if valores[i] == maiscaro:
        print(f"O produto mais caro é {produto[i]} e custa {maiscaro} reais")
        break
for i in range(15):
    if valores[i] == maisbarato:
        print(
            f"O produto mais barato é {produto[i]} e custa {maisbarato} reais")
        break
n = str(input())
for i in range(15):
    if n == produto[i]:
        print("O valor desse produto é", valores[i])
