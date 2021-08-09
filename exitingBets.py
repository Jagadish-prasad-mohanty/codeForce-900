def bet(a,b):
    if a==b:
        return [0,0]
    else:
        diff=abs(a-b)
        s=a%diff
        if s > diff-s:
            return [diff,diff-s]
        else:
            return [diff,s]

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    res=bet(a,b)
    print(res[0],res[1])
