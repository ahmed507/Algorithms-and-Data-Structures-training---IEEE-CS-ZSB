n,m,c = input().split()
out = []
all_desks = []
for i in range(int(n)):
    all_desks.append(input())
for i in range(int(n)):
    for j in range(int(m)):
        if all_desks[i][j] == c:
            if i!=0 and all_desks[i-1][j]!=c and all_desks[i-1][j]!='.' and all_desks[i-1][j] not in out:
                out.append(all_desks[i-1][j])
            if i!=int(n)-1 and all_desks[i+1][j]!=c and all_desks[i+1][j]!='.' and all_desks[i+1][j] not in out:
                out.append(all_desks[i+1][j])
            if j!=0 and all_desks[i][j-1]!=c and all_desks[i][j-1]!='.' and all_desks[i][j-1] not in out:
                out.append(all_desks[i][j-1])
            if j!=int(m)-1 and all_desks[i][j+1]!=c and all_desks[i][j+1]!='.' and all_desks[i][j+1] not in out:
                out.append(all_desks[i][j+1])
print(len(out))