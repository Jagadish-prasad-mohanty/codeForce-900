def getMaxmOp(n):
    i=9
    res=0
    inc=0
    if n>45:
        return -1
    if n==45:
        return 123456789
    while(n>0):
        if n>i:
            n-=i
            res+=i*(10**inc)
        else:
            res+=n*(10**inc)
            n=0
        i-=1
        inc+=1

    return res



t=int(input())
while t:
    n=int(input())
    res=getMaxmOp(n)
    print(res)
    t-=1