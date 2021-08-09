def split(n,k,arr):
    if k*2+1>n:
        return "NO"
    if k==0:
        return "YES"
    count=0
    i=0
    j=n-1
    while(i<j):
        if arr[i]==arr[j]:
            count+=1
        else:
            break

        i+=1
        j-=1

    if count <k:
        return "NO"
    else:
        if count==k and count*2<n:
            return "YES"
        elif count>k:
            return "YES"
        else:
            return "NO"


        
    

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=input()
    print(split(n,k,arr))
