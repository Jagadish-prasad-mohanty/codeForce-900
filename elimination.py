def elimination(a,b,c,d):
    return max(a+b,c+d)


t=int(input())
while t:
    a,b,c,d=map(int,input().split())
    print(elimination(a,b,c,d))
    t-=1