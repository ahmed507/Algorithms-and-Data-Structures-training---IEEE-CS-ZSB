from math import ceil

a, x, y = map(int, input().split())
cases = [1]
i = 2
level = ceil(y / a)
squares = 1

if y == 0 or y % a == 0 or abs(x) >= a :
    print(-1)
else:
    if level == 1:
        if abs(x) >= ((a+1)//2):
            print(-1)
        else:
            print(1)
    elif level % 2 != 0:
        if x == 0:
            print(-1)
        else:
            for i in range(2, level + 1):
                if i % 2 == 0:
                    squares += 1
                else:
                    squares += 2
            if x < 0:
                squares -=1
            print(squares)
    else:
        if abs(x) >= ((a + 1) // 2):
            print(-1)
        else:
            for i in range(2, level + 1):
                if i % 2 == 0:
                    squares += 1
                else:
                    squares += 2

            print(squares)
