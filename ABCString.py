def checkValidity(st):
    count=0
    for i in st:
        if i=='(':
            count+=1
        else:
            count-=1
        if count <0:
            return False
    if count!=0:
        return False
    else:
        return True
def match(a):
    first=a[0]
    last=a[-1]

    b=''
    for i in range(len(a)):
        if a[i]==first:
            b+='('
        elif a[i]==last :
            b+=')'
        else:
            b+='('
    # print("[first]",b)
    if checkValidity(b):
        return 'YES'
    b=''
    for i in range(len(a)):
        if a[i]==first:
            b+='('
        elif a[i]==last :
            b+=')'
        else:
            b+=')'
    # print('[last]',b)
    if checkValidity(b):
        return 'YES'
    else:
        return 'NO'

t=int(input())
for i in range(t):
    a=input()
    print(match(a))



    