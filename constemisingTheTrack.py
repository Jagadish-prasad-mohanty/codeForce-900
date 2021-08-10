def track(arr,n):
    summ=sum(arr)
    if summ==n:
        return 0
    else:
        rem=sum(arr)%n
        return rem*(n-rem)
        

    return sum

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(track(arr,n))
