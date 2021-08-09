# def isIncreasable(arr,n):
#     while(True):
#         flag=0
#         for i in range(n-1):
#             if(arr[i]>=arr[i+1]):
#                 if(arr[i]>0):
#                     arr[i]-=1
#                     arr[i+1]+=1
#                     flag=1
#                 else:
#                     return 0

#         if(flag==0):
#             return 1
def isIncreasable(arr,n):
    ex=0
    for i in range(n):
        if arr[i]>i:
            ex+=arr[i]-i
        elif arr[i]<i:
            ex-=(i-arr[i])
            if ex<0:
                return 0
    return 1




t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if(isIncreasable(arr,n)):
        print("YES")
    else:
        print("NO")

    t-=1