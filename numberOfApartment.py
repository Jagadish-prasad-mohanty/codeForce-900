def getCount(n):
    if n==1 or n==2 or n==4:
        return [-1]*3
    a=b=c=0
    c=n//7
    n%=7
    if n==1 or n==2 or n==4:
        n+=7
        c-=1
        if n==8:
            a+=1
            b+=1
        elif n==9:
            a+=3
        else:
            a+=2
            b+=1

    else:
        if n%3==0:
            a+=n//3

        else:
            b+=1

    return [a,b,c]

t=int(input())
while t:
    n=int(input())
    res=getCount(n)
    if res[0]==-1:
        print(-1,end=" ")
    else:
        for i in res:
            print(i,end=" ")
    print()
    t-=1