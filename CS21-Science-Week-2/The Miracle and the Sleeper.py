import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a > b/2:
        print(b%a)
    else:
        print(math.ceil((b/2)-1))