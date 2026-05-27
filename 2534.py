while True:
    try:
        n, q = map(int, input().split())
        notas_habitantes = []
        for i in range(n):
            ni = int(input())
            notas_habitantes.append(ni)
        notas_habitantes.sort(reverse=True)
        for i in range(q):
            p = int(input())
            print(notas_habitantes[p-1])
    except EOFError:
        break
