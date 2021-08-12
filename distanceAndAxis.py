def dis(n,k):
    if (k==0 and n%2==0) or n==k:
        return 0
    elif k==0 and n%2==0:
        return 1
    elif n==0:
        return k
    elif n<k:
        return k-n
    elif n>k:
        if (n%2==0 and k%2==0) or (n%2!=0 and k%2!=0):
            return 0
        else:
            return 1

for i in range(int(input())):
    n,k=map(int,input().split())
    print(dis(n,k))