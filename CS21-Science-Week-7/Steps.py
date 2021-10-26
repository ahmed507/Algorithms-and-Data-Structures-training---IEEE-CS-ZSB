n,m = map(int,input().split())
init_x,init_y = map(int,input().split())
k = int(input())
total_steps = 0
for i in range(k):
    x,y=map(int,input().split())
    steps_x,steps_y=10**9,10**9
    if x>0:
        steps_x = (n-init_x)//x
    elif x<0:
        steps_x = (init_x-1)//(-1*x)
    if y>0:
        steps_y = (m-init_y)//y
    elif y<0:
        steps_y = (init_y-1)//(-1*y)
    steps = 0
    if steps_x>0 and steps_y>0:
        steps = min(steps_x,steps_y)
    init_x += steps*x
    init_y += steps*y
    total_steps += steps

print(total_steps)

