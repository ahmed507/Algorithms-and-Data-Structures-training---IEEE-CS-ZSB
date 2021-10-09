t = int(input())
for i in range(t):
    n = int(input())
    c1 = (n//3) + (n-(n//3))%2
    c2 = ((n-(n//3)) - (n-(n//3))%2)//2
    print(c1,c2)