import math
a,b,c,d = map(int,input().split())
if a/b > c/d:
    x = a*d -b *c
    y=a*d

else:
    x = b * c-a*d
    y = b*c

z=math.gcd(x,y)
x//=z
y//=z
print(str(x)+"/"+str(y))
