def is_equal(a):
    if len(a) <= 2:
        return True
    elif len(a)==3:
        if a[0]+a[2]==2*a[1]:
            return True
        else:
            return False
    else:
        return False


n = int(input())
a = list(map(int, input().split()))
a.sort()
a = list(dict.fromkeys(a))
if is_equal(a):
    print("YES")
else:
    print("NO")


