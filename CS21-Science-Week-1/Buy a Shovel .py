k, r = map(int, input().split())
i = 1
while True:
    if i * k % 10 == 0 or i * k % 10 == r:
        print(i)
        break
    i += 1