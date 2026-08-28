n=int(input("Enter a number: "))
nod=len(str(n))
num=n
total=0
while num>0:
    total=total+((num%10)**nod)
    num=num//10
if total==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")