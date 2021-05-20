def getFinalCake(lis,n):
    li= [0]*n
    for i in range(n):
        li[i]+=2
        rg=i-lis[i]
        if rg<0:
            rg=-1
        for j in range(i,rg,-1):
            li[j]-=1

    for i in range(len(li)):
         if li[i]<1:
                li[i]=1
    for i in range(len(li)):
        if li[i]==2:
            li[i]=0
       

    return li


## 1 1 2 1 0 1
#i=5
#rg=2

t=int(input())
for _ in range(t):
    n=int(input())
    lis=list(map(int,input().split()))
    for i in getFinalCake(lis,n):
        print(i,end=" ")
