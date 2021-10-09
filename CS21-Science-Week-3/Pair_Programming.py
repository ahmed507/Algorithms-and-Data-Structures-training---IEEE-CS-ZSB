t = int(input())
for _ in range(t):
    input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    i = 0
    j = 0
    out = []
    while i < n or j < m:
        if i < n and j < m:
            if a[i] == 0:
                out.append(a[i])
                i += 1
                k += 1
            elif b[j] == 0:
                out.append(b[j])
                j += 1
                k += 1
            else:
                if a[i] < b[j] and a[i] <= k:
                    out.append(a[i])
                    i += 1
                elif a[i] >= b[j] and b[j] <= k:
                    out.append(b[j])
                    j += 1
                else:
                    print(-1)
                    break
        elif i < n:
            if a[i] == 0:
                out.append(a[i])
                i += 1
                k += 1
            else:
                if a[i] <= k:
                    out.append(a[i])
                    i += 1
                else:
                    print(-1)
                    break
        elif j < m:
            if b[j] == 0:
                out.append(b[j])
                j += 1
                k += 1
            else:
                if b[j] <= k:
                    out.append(b[j])
                    j += 1
                else:
                    print(-1)
                    break
        if len(out) == n + m:
            for i in out:
                print(i, end=" ")
            print()
