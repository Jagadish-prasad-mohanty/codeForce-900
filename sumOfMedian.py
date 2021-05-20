import math
def maxSumOfMedian(n,k,li):
    length=len(li)
    median=math.ceil(n/2)
    start=(median-1)*k
    sum=li[start]
    for i in range(1,k):
        sum+=li[start+(n-median+1)*i]

    return sum


t=int(input())
while t:
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    print(maxSumOfMedian(n,k,li))
    t-=1