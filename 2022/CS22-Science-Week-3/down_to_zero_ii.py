import math

def downToZero(n):
    def isprime(num):
        if num==2 or num==3:
            return True
        if num%2==0 or num<2:
            return False
        for n in range(3,int(math.sqrt(num))+1,2):
            if num%n==0:
                return False
        return True
    count=0
    while n!=1:
        if isprime(n):
            n-=1
            count+=1
        else:
            k=2
            while n%k!=0 and n/k!=1:
                k+=1
            count+=1
            n=n-n/k
    return count+1