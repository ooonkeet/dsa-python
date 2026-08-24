n=int(input("Enter number: "))
num=n
count=0
while num>0:
    mod=num%10
    count+=1
    num=num//10
print("Number of digits in",n,"is",count)