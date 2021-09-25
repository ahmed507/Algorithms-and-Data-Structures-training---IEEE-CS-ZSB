n, d = map(int, input().split())
friends = []

for _ in range(n):
    m, s = map(int, input().split())
    friends.append([m, s])

friends = sorted(friends, key=lambda x: x[0])
max_total = 0
l = 0
r = 0
temp = 0
while r < len(friends):
    if abs(friends[l][0] - friends[r][0]) < d:
        temp += friends[r][1]
        r += 1
    else:
        temp -= friends[l][1]
        max_total = max(max_total, temp)
        l += 1
    max_total = max(max_total, temp)
print(max_total)
