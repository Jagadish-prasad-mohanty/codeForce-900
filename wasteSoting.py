def isStorable(c,a):
    if c[0]-a[0] >=0 and c[1]-a[1] >=0 and c[2]-a[2] >=0:
        c[0]-=a[0]
        c[1]-=a[1]
        c[2]-=a[2]
    else:
        return False
    if c[0]-a[3] <0:
        a[3]-=c[0]
        if c[2]-a[3]<0:
            return False
        else:
            c[2]-=a[3]

    if c[1]-a[4] <0:
        a[4]-=c[1]
        if c[2]-a[4]<0:
            return False
    
    return True



t=int(input())
while t:
    c=list(map(int,input().split()))
    a=list(map(int,input().split()))
    if(isStorable(c,a)):
        print("YES")
    else:
        print("NO")
    t-=1