q = int(input())
queue = []
for i in range(q):
    x = list(map(int,input().split()))
    if x[0] == 1:
        queue.append(x[1])
    elif x[0]== 2:
        queue.pop(0)
    elif x[0] == 3:
        print(queue[0])