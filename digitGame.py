def digitGame(num,n):
    st=str(num)
    
    check=0
    ev=[]
    od=[]
    for i in range(n):
        if check==0:
            od.append(int(st[i]))
            check=1
        else:
            ev.append(int(st[i]))
            check=0
    # print(od,ev)

    flag=0   
    if n%2==0:
        for i in ev:
            if i%2==0:
                flag=2
                break
        if flag==0:
            flag=1
    
    else:
        flag=0
        for i in od:
            if i%2!=0:
                flag=1
                break
        if flag==0:
            flag=2
    if flag==1:
        return 1
    elif flag==2:
        return 2

t=int(input())
for i in range(t):
    n=int(input())
    num=int(input())
    print(digitGame(num,n))
