n = int(input())
resto = 0
if n > 0:
    for i in range(1, 10001):
        if i % n == 2:
            print(i)
