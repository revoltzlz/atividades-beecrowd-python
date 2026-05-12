a, b, c = map(float, input().split())
soma = a+b+c
if (a > 0 and
    b > 0 and
    c > 0 and
    (a+b) > c and
    (a+c) > b and
        (b+c) > a):
    print(f"Perimetro = {soma:.1f}")
else:
    area = ((a+b)*c)/2
    print(f"Area = {area:.1f}")
