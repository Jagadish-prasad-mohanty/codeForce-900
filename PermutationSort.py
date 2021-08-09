def pSort(arr,n):
    flag=0
    for i in range(n):
        if arr[i]!=i+1:
            flag=1
            break
    if flag==0:
        return 0
    elif arr[0]==n:
        if arr[n-1]==1:
            return 3
    
    elif arr[0]==1 or arr[n-1]==n:
        return 1 
    else:
        return 2

   

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(pSort(arr,n)) 

