a = float(input())
if (a > 0 and a <= 400):
    p1 = a*0.15
    primeiro = p1+a
    print(f"Novo salario: {primeiro:.2f}")
    print(f"Reajuste ganho: {p1:.2f}")
    print("Em percentual: 15 %")

elif (a > 0 and a <= 800):
    p2 = a*0.12
    segundo = p2+a
    print(f"Novo salario: {segundo:.2f}")
    print(f"Reajuste ganho: {p2:.2f}")
    print("Em percentual: 12 %")

elif (a > 0 and a <= 1200):
    p3 = a*0.1
    terceiro = p3+a
    print(f"Novo salario: {terceiro:.2f}")
    print(f"Reajuste ganho: {p3:.2f}")
    print("Em percentual: 10 %")

elif (a > 0 and a <= 2000):
    p4 = a*0.07
    quarto = p4+a
    print(f"Novo salario: {quarto:.2f}")
    print(f"Reajuste ganho: {p4:.2f}")
    print("Em percentual: 7 %")

else:
    p5 = a*0.04
    quinto = p5+a
    print(f"Novo salario: {quinto:.2f}")
    print(f"Reajuste ganho: {p5:.2f}")
    print("Em percentual: 4 %")
