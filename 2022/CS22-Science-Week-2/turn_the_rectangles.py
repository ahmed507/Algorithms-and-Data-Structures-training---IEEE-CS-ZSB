n = int(input())
x = 0
nonAscending = True
for i in range(n):
    w, h = map(int, input().split())
    if x == 0:
        x = max(w, h)
    else:
        if x >= h and x >= w:
            x = max(w, h)
        elif x >= h:
            x = h
        elif x >= w:
            x = w
        else:
            nonAscending = False
            break
if nonAscending:
    print("YES")
else:
    print("NO")
