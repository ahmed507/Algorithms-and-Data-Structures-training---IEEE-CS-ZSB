from math import ceil

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    new_str = ""
    i = 0
    while i < n:
        new_str += s[i]
        j = i
        while i < n and s[i] == s[j]:
            i += 1
    if b < 0:
        print(a * n + ceil((len(new_str) + 1) / 2) * b)
    else:
        print(n * (a + b))
