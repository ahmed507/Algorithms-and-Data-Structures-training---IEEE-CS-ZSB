d = int(input())
n = int(input())
a = list(map(int,input().split()))
c = 0
for i in range(len(a)-1):
    if a[i]<d:
        c+=d-a[i]
print(c)