a, b, c = map(int, input().split())
if a > b and b <= c:
    print(':)')
elif a < b and b >= c:
    print(':(')
elif a > b and b > c:
    if (b-a) > (c-b):
        print(':(')
    elif (b-a) < (c-b):
        print(':)')
elif a < b and b < c:
    if (a-b) > (b-c):
        print(':)')
    elif (a-b) < (b-c):
        print(':(')
elif a == b and b < c:
    print(':)')
elif a == b and b > c:
    print(':(')
