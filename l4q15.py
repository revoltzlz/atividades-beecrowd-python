conta = []
agencia = []
saldos = []

for i in range(100):
    c = int(input())
    conta.append(c)
    a = int(input())
    agencia.append(a)
    s = float(input())
    saldos.append(s)

for i in range(100):
    print(f"Conta: {conta[i]}")
    if saldos[i] > 0:
        print(f"Saldo positivo de: {saldos[i]:.2f}")
    else:
        print(f"Saldo negativo de: {saldos[i]:.2f}")

for ag in set(agencia):
    total_clientes = 0
    negativos = 0

    for i in range(100):
        if agencia[i] == ag:
            total_clientes += 1
            if saldos[i] < 0:
                negativos += 1

    percentual = (negativos/total_clientes)*100
    print(f"\nAgência: {ag}")
    print(f"Clientes: {total_clientes}")
    print(f"Negativos: {percentual:.2f}%")
