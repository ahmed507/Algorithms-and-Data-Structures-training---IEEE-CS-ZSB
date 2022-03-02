n = int(input())
b = list(map(int, input().split()))
b = sorted(b, reverse=True)
# print(b)
l, r = [], []
m = b[0]
b1 = []
for i in b:
    if i != m:
        b1.append(i)

for i in range(len(b1)):
    if i % 2 == 0:
        if len(r) == 0:
            r.append(b1[i])
        else:
            if b1[i] != r[-1]:
                r.append(b1[i])
    elif i % 2 == 1:
        if len(l) == 0:
            l.append(b1[i])
        else:
            if b1[i] != l[-1]:
                l.append(b1[i])
l = sorted(l)
l.append(m)
# print(r)
out = l + r
print(len(out))
for x in out:
    print(x, end=" ")
