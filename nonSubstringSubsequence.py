def isSubstringSubsequence(s,n,l,r):
    first=s[l-1]
    second=s[r-1]

    if first in s[:l-1]:
        return True
    
    if second in s[r:]:
        return True

    return False


t=int(input())
while t:
    n,q=map(int,input().split())
    s=input()
    while q:
        l,r=map(int,input().split())
        if isSubstringSubsequence(s,n,l,r):
            print("YES")
        else:
            print("NO")
        q-=1

    t-=1