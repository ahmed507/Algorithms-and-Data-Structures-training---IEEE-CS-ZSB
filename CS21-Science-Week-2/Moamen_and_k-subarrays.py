t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = []
    c = 1
    for i in range(n):
        s += [[a[i],i]]
    s.sort()
    for i in range(1,n):
        if s[i][1] != s[i-1][1]+1:
            c += 1
    if c <= k:
        print("YES")
    else:
        print("NO")