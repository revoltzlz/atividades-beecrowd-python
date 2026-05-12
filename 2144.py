def calcula_1rm(w, r):
    return w * (1 + r / 30)


medias = []

while True:
    w1, w2, r = map(int, input().split())

    if w1 == 0 and w2 == 0 and r == 0:
        break

    m1 = calcula_1rm(w1, r)
    m2 = calcula_1rm(w2, r)

    M = (m1 + m2) / 2
    medias.append(M)

    if 1 <= M < 13:
        print("Nao vai da nao")
    elif 13 <= M < 14:
        print("E 13")
    elif 14 <= M < 40:
        print("Bora, hora do show! BIIR!")
    elif 40 <= M <= 60:
        print("Ta saindo da jaula o monstro!")
    elif M > 60:
        print("AQUI E BODYBUILDER!!")

# Média final
if len(medias) > 0:
    media_final = sum(medias) / len(medias)

    if media_final > 40:
        print()
        print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")
