A, B, C = map(int, input().split())

d1 = B - A
d2 = C - B


if d1 < 0 and d2 >= 0:
    print(":)")

elif d1 > 0 and d2 <= 0:
    print(":(")

elif d1 > 0 and d2 > 0:
    if d2 < d1:
        print(":(")
    else:
        print(":)")

elif d1 < 0 and d2 < 0:
    if d2 > d1:
        print(":)")
    else:
        print(":(")

else:
    if d2 > 0:
        print(":)")
    else:
        print(":(")
