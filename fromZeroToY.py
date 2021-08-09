def zeroToY(x,y):
    res=0
    rem=0
    power=0
    while x<=y:
        rem=y//x
        power=len(str(rem))-1
        res+=y//(x*(10**power))
        # print(res)
        y%=(x*(10**power))
    res+=y
    return res




t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(zeroToY(x,y))