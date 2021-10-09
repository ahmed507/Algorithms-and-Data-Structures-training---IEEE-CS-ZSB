def bcd(n,a,t):
    current_index =  a-1
    counter = t[current_index]
    l = current_index - 1
    r = current_index + 1
    while l>=0 and r<n:
        if t[l]>=1 and t[r]>=1:
            counter += t[l]
            counter += t[r]
        l -=1
        r+=1
    if l ==-1:
        for i in range(r,n):
            counter+=t[i]
    elif r == n:
        for i in range(0,l+1):
            counter +=t[i]
    return counter



n,a = map(int,input().split())
t = list(map(int,input().split()))
print(bcd(n,a,t))