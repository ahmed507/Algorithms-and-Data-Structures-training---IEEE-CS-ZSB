n = int(input())
l = list(map(int,input().split()))
counter = 0
x1 = 0
x2 = 0
for i in range(len(l)):
    if l[i] == i:
        counter+=1
    else:
        if i == l[l[i]]:
            x1 = 2
if x1 == 0:
    for j in range(len(l)):
        if j!=l[j] and j in l:
            x1 = 1
            break

print(counter+x1+x2)
# for j in range(len(l)):
#     if l[j]!=j:
#         x=[]
# print(counter)