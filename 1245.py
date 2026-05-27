while True:
    try:
        n = int(input())

        esquerdo = [0] * 61
        direito = [0] * 61

        for i in range(n):
            tamanho, lado = input().split()
            tamanho = int(tamanho)

            if lado == 'E':
                esquerdo[tamanho] += 1
            else:
                direito[tamanho] += 1

        pares = 0

        for i in range(30, 61):
            if esquerdo[i] < direito[i]:
                pares += esquerdo[i]
            else:
                pares += direito[i]

        print(pares)

    except EOFError:
        break
