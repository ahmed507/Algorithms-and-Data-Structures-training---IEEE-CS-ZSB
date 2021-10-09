def xor(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if xor(a - 1) == b:
        print(a)
    else:
        if xor(a - 1) ^ b == a:
            print(a + 2)
        else:
            print(a + 1)
