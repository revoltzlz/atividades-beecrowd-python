l, a, p, r = map(int, input().split())
diagonal = (l**2 + a**2 + p**2)**(1/2)
diametro = 2*r

if diagonal <= diametro:
    print("S")
else:
    print("N")
