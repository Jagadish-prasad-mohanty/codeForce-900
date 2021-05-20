# def getDominantPirana(n,arr):
#     maxm=arr[0]
#     maxmIndex=0
#     flag=0
#     for i in range(1,n-1):
#         if (arr[i]>arr[i+1] and arr[i]>=arr[i-1] ) or (arr[i]>arr[i-1] and arr[i]>=arr[i+1]):
#             if(maxm<=arr[i]):
#                 maxm=arr[i]
#                 maxmIndex=i

#         if maxm!=arr[i]:
#             flag=1

#     if maxm!=arr[n-1]:
#         flag=1
#     if(arr[n-1]>maxm):
#         maxm=arr[n-1]
#         maxmIndex=n-1


#     if flag==1:
#         return maxmIndex+1
#     else:
#         return -1


def getDominantPirana(n,arr):
    maxm=0
    maxmIndex=-1
    ctMaxm=1
    reqIndex=-1
    for i in range(n):
        if arr[i]>maxm:
            maxm=arr[i]
            ctMaxm=1
            maxmIndex=i
            reqIndex=i-1
        elif arr[i]==maxm:
            ctMaxm+=1
            maxmIndex=i

        else:
            reqIndex=i

    # print(reqIndex)
    if ctMaxm==n:
        return -1

    if reqIndex==-1:
        return maxmIndex+1

    for i in range(reqIndex,n):
        if arr[i]==maxm:
            return i+1
    for i in range(reqIndex,-1,-1):
        if arr[i]==maxm: 
            return i+1




  


        




t=int(input())
while t:
    n=int(input())
    arr=list(map(int,input().split()))
    res=getDominantPirana(n,arr)
    print(res)
    t-=1

