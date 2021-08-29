n = list(map(int, list(input())))
k = 0
while "".join(list(map(str,n))) != '1':
    if len(n) == 1:
        break
    n = list(map(int,list(str(sum(n)))))
    k +=1
print(k)
