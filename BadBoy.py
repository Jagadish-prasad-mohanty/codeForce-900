# def BadBoy(n,m,i,j):
#     maxm=[0,0]
#     store=[(0,0),(0,0)]
#     for a in range(1,n+1):
#         for b in range(1,m+1):
#             if abs(a-i)+abs(b-j)>maxm[1] and abs(a-store[1][0])+abs(b-store[1][1])>abs(store[1][0]-store[0][0])+abs(store[1][1]-store[0][1]):
#                 maxm[0]=maxm[1]
#                 maxm[1]=abs(a-i)+abs(b-j)
#                 store[0]=store[1]
#                 store[1]=(a,b)
#             elif abs(a-i)+abs(b-j)>maxm[0]:
#                 maxm[0]=abs(a-i)+abs(b-j)
#                 store[0]=(a,b)

#     return store

def BadBoy(n,m,i,j):
    if n==1 or m==1:
        return [(n,m),(1,1)]
    a=n//2
    b=m//2
    if i<=a and j<=b:
        return [(1,m),(n,1)]
    elif i<=a and j>b:
        return [(1,1),(n,m)]
    elif i>a and j<=b:
        return [(1,1),(n,m)]
    elif i>a and j>b:
        return [(1,m),(n,1)]




t=int(input())
for i in range(t):
    n,m,i,j=map(int,input().strip().split())

    ans=BadBoy(n,m,i,j)

    for a in ans:
        for b in a:
            print(b,end=" ")
    print()
    