n=int(input("Enter a number: "))
num=n
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==n:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")