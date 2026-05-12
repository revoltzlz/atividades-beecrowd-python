qtdcaixa = int(input())
peso = []
precouni = []
for i in range(qtdcaixa):
    kg = float(input())
    peso.append(kg)
for i in range(qtdcaixa):
    rs = float(input())
    precouni.append(rs)
total = float(input())
print(f"O peso total é: {sum(peso):.2f} kg")
print(f"O preço total é: {sum(precouni):.2f} reais")
if sum(precouni) != total:
    print("Existe conflito entre a soma do valor total de todas as caixas por unidade e valor total informado")
else:
    print("Os valores conferem, está tudo certo!")
