def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter a number to find fibonacci series upto that number: "))
for i in range(n):
    print(fibo(i),end=" ")

# example of simple recursion to find fibonacci series upto n
# time complexity - O(2^N) and space complexity - O(N)