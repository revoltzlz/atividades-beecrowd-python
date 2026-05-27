while True:
    try:
        n = int(input())

        m, l = map(int, input().split())

        marcos = []
        leonardo = []

        for i in range(m):
            carta = list(map(int, input().split()))
            marcos.append(carta)

        for i in range(l):
            carta = list(map(int, input().split()))
            leonardo.append(carta)

        cm, cl = map(int, input().split())

        a = int(input())

        valor_marcos = marcos[cm - 1][a - 1]
        valor_leonardo = leonardo[cl - 1][a - 1]

        if valor_marcos > valor_leonardo:
            print("Marcos")

        elif valor_leonardo > valor_marcos:
            print("Leonardo")

        else:
            print("Empate")

    except EOFError:
        break
