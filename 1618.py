n = int(input())

for i in range(n):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int, input().split())

    if Ax <= Rx <= Bx and Ay <= Ry <= Dy:
        print("1")

    else:
        print("0")
