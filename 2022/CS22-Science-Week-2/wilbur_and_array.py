n = int(input())
a = [0] * n
b = list(map(int, input().split()))
x = b[0] - a[0]
counter = abs(x)
for i in range(1, n):
    if x != b[i]:
        counter += abs(b[i] - x)
        x+=b[i]-x

print(counter)
