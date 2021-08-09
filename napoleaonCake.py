# def getFinalCake(lis,n):
#     li= [0]*n
#     for i in range(n):
#         if lis[i]!=0:
#             lim=-1
#             if i-lis[i]>=0:
#                 lim=i-lis[i]
#             for j in range(i,lim,-1):
#                 li[j]+=1
#     for i in range(n):
#         if li[i]>0:
#             li[i]=1

#     return li
def getFinalCake(lis,n):
    li=[1]*n
    i=n-1
    x=n
    while i>=0:
        if lis[i]>0:
            if x>i-lis[i]+1:
                x=i-lis[i]+1
        if i<x:
            li[i]=0

        i-=1
            

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
    print()
