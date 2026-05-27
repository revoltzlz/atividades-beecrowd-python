while True:
    try:
        impeachment = 0
        n = int(input())
        votos = list(map(int, input().split()))
        for valor in votos:
            if valor == 1:
                impeachment += 1
        if impeachment >= (n*2)/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
