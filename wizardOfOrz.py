def getMaxmOp(n):
    if(n==1):
        return 9
    if n==2:
        return 98
    res="98"
    inc=9
    for i in range(n-2):
        res=res+str(inc)
        if inc==9:
            inc=0
        else:
            inc+=1

    return res

t=int(input())
while t:
    n=int(input())
    res=getMaxmOp(n)
    print(res)
    t-=1