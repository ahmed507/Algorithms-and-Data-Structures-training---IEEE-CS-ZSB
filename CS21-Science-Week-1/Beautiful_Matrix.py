arr = []
one_arr = []
one_i_index = 0
one_j_index = 0
numOfMoves = 0
for n in range(5):
    a, b, c, d, e = map(int, input().split())
    arr.append([a, b, c, d, e])
for i in range(len(arr)):
    if sum(arr[i]) == 1:
        one_i_index = i
        one_arr = arr[i]
for j in range(len(one_arr)):
    if one_arr[j] == 1:
        one_j_index = j
numOfMoves = abs(one_i_index - 2) + abs(one_j_index - 2)
print(numOfMoves)