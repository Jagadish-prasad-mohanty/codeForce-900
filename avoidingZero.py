def getRes(n,lis):
    pos=[]
    neg=[]
    c=0
    msum=0
    for i in lis:
        msum+=i
        if i>0:
            pos.append(i)
        elif i==0:
            c+=1
        else:
            neg.append(i)

    # print(sum(pos),sum(neg))
    if msum==0:
        return []
    res=[]
    checkSum=0
    if sum(pos) > abs(sum(neg)):
    
        # print(pos,neg)
        # print('hi')
        for i in pos:
            res.append(i)

        for i in neg:
            res.append(i)

        for i in range(c):
            res.append(0)
    elif sum(pos) < abs(sum(neg)):

        # print(pos,neg)
        

        for i in neg:
            res.append(i)

        for i in pos:
            res.append(i)

        for i in range(c):
            res.append(0)

    return res


t=int(input())
while t:
    n=int(input())
    lis=list(map(int,input().split()))
    res=getRes(n,lis)
    if len(res):
        print("YES")
        print(' '.join(map(str,res)))
    else:
        print("NO")
    t-=1