def mergeSort(arr,l,r,tempArr):
    count=0
    if l<r:
        mid=(l+r)//2
        count+=mergeSort(arr,l,mid,tempArr)
        count+=mergeSort(arr,mid+1,r,tempArr)
        count+=merge(arr,tempArr,l,mid,r)
    return count

def merge(arr,tempArr,l,mid,r):
    count=0
    i=k=l
    j=mid+1
    while i<=mid and j<=r:
        if arr[i]<=arr[j]:
            tempArr[k]=arr[i]
            k+=1
            i+=1

        else:
            count+=(mid-i+1)
            tempArr[k]=arr[j]
            j+=1
            k+=1
    while j<=r:
        tempArr[k]=arr[j]
        j+=1
        k+=1
    while i<=mid:
        tempArr[k]=arr[i]
        k+=1
        i+=1
    for i in range(l,r+1):
        arr[i]=tempArr[i]
    return count

def cSort(arr,n):
    tempArr=[0]*n
    req=n*(n-1)//2
    count=mergeSort(arr,0,n-1,tempArr)
    # print(count)
    if count<req:
        return 'YES'
    else:
        return 'NO'

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(cSort(arr,n))
            

        