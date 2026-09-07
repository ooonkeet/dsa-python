def func(sum,i,N):
    if i>N:
        print("Sum of first N natural numbers is: ",sum)
        return
    return func(sum+i,i+1,N)
func(0,1,12)

def fun(N):
    if N==1:
        return 1
    return N+fun(N-1)
N=int(input("Enter a number to find sum of first N natural numbers: "))
print("Sum of first N natural numbers is: ",fun(N))