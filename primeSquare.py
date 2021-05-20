
def printPrimeSquare(n):
    for i in range(n):
        for j in range(n):
            if(j==i or j==i+1 or (j==0 and i==n-1)):
                print(1,end=" ")
            else:
                print(0,end=" ")

        print()


t=int(input())
while t:
    n=int(input())
    printPrimeSquare(n)

    t-=1