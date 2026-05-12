a, b = map(int, input().split())
if (a < b):
    sub = b-a
    print(f"O JOGO DUROU {sub} HORA(S)")
else:
    caso2 = (24-a) + b
    print(f"O JOGO DUROU {caso2} HORA(S)")
