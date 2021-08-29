letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w',
           'x', 'y', 'z')

n, q = map(int, input().split())
s = input()
sums = [0]
for k in range(len(s)):
    sums.append(sums[k]+letters.index(s[k])+1)
for i in range(q):
    l, r = map(int, input().split())
    print(sums[r]-sums[l-1])
