z = []
x = []
p, q, l, r = map(int, input().split())
for i in range(p):
    a, b = map(int, input().split())
    z.append([a, b])
for i in range(q):
    a, b = map(int, input().split())
    x.append([a, b])
out = 0
for i in range(l, r + 1):
    counter = 0
    for j in z:
        for k in x:
            if j[0] <= k[1] + i and j[1] >= k[0] + i:
                counter = 1
    out += counter
print(out)
