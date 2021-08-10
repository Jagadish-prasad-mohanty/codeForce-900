def pizzaForce(n):
    div=n//6
    rem=n%6
    if div==0:
        return 15
    if rem==0:
        return div*15

    elif rem<=2:
        return (div-1)*15+20
        
    elif rem<=4:
        return (div-1)*15+25
    else:
        return (div+1)*15

t=int(input())
for i in range(t):
    n=int(input())
    print(pizzaForce(n))