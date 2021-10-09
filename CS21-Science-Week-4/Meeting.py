def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def check(x, y, n, xi, yi, r):
    for i in range(n):
        if dist(x, y, xi[i], yi[i]) <= r[i] ** 2:
            return 0
    return 1


Xa, Ya, Xb, Yb = map(int, input().split())
n = int(input())
Xi = [None] * n
Yi = [None] * n
R = [None] * n
ans = 0
for i in range(n):
    Xi[i], Yi[i], R[i] = map(int, input().split())
j = min(Xa, Xb)
k = min(Ya, Yb) + 1

for j in range(min(Xa, Xb), max(Xa, Xb)+1):
    ans += check(j, Ya, n, Xi, Yi, R) + check(j, Yb, n, Xi, Yi, R)
for k in range(min(Ya, Yb)+1, max(Ya, Yb)):
    ans += check(Xa, k, n, Xi, Yi, R) + check(Xb, k, n, Xi, Yi, R)

print(ans)
