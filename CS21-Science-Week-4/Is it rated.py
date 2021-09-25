def is_rated(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return "rated"
    for j in range(1, len(a)):
        if a[j] > a[j-1]:
            return "unrated"
    return "maybe"


n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(is_rated(a, b))
