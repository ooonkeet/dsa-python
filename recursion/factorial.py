def fact(N):
    if N==1 or N==0:
        return 1
    return N*fact(N-1)
N=int(input("Enter a number to find factorial: "))
print("Factorial of ",N," is: ",fact(N))

# example of simple recursion to find factorial of a number
# tc - O(N) sc - O(N) stack space