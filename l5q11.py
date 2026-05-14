media = sum(TEMPERATURAS)/len(TEMPERATURAS)
inferiorm = 0
menor20 = 0
maior35 = 0
for i in range(len(TEMPERATURAS)):
    if TEMPERATURAS[i] < media:
        inferiorm += 1
for i in range(len(TEMPERATURAS)):
    if TEMPERATURAS[i] < 20:
        menor20 += 1
for i in range(len(TEMPERATURAS)):
    if TEMPERATURAS[i] > 35:
        maior35 += 1
print("Temp media:", media)
print("numero de dias com temp menor que a media", inferiorm)
print("Numero de dias que fez menos de 20 graus:", menor20)
print("Numero de dias que fez mais de 35 graus", maior35)
