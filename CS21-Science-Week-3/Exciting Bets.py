t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(abs(a - b), 0)
    else:
        print(abs(a - b), min(a % abs(a - b), abs(a - b) - a % abs(a - b)))
