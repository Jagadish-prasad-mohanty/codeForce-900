def GCD(a,b):
    if a==b:
        return a
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return GCD(b,a%b)
    return GCD(a,b%a)


def ArrayReordering(arr,n):
    res=[]
    for i in range(n):
        if arr[i]%2==0:
            res.append(arr[i])
    for i in range(n):
        if arr[i]%2!=0:
            res.append(arr[i])
    count=0  
    for i in range(n):
        for j in range(i+1,n):
            if GCD(res[i],2*res[j])>1:
                count+=1
    return count


    


t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(ArrayReordering(arr,n))