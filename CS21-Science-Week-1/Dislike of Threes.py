l = []
i = 0
while len(l)!=1000:
    if i%3 != 0 and str(i)[-1] != "3":
        l.append(i)
    i += 1

n = int(input())
for i in range(n):
    print(l[int(input())-1])