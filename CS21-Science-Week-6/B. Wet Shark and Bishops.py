n=int(input())
add = [0]*2001
sub = [0]*2001
counter = 0
for i in range(n):
    x,y = map(int,input().split())
    counter += add[x+y]
    add[x + y] += 1
    counter += sub[x-y]
    sub[x-y] += 1
print(counter)