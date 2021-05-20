import math
def isGreatHero(A,B,n,a,b):
    i=0
    a,b = zip(*sorted(zip(a,b)))
    for i in range(n):
        noOfHitToDieEnemy=math.ceil(b[i]/A)
        noOfHitToDieHero=math.ceil(B/a[i])
        if(noOfHitToDieEnemy<=noOfHitToDieHero):
            B-=noOfHitToDieEnemy*a[i]
        else:
            return False

        if(B<=0):
            break

    if(i==n-1):
        return True
    else:
        return False




t=int(input())
while t:
    A,B,n=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(isGreatHero(A,B,n,a,b)):
        print("YES")
    else:
        print("NO")
    t-=1
