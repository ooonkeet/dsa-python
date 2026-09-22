m=int(input("Enter a number = "))
n=int(input("Enter another number = "))
# and operator
print(m,"and",n,"gives",m&n)
# or operator
print(m,"or",n,"gives",m|n)
# xor operator
print(m,"xor",n,"gives",m^n)
# not operator
print("not",m,"gives",~(m))
print("not",n,"gives",~(n))
print(m,"right shifted by",n,"gives",abs(m)>>abs(n))
print(m,"left shifted by",n,"gives",abs(m)<<abs(n))


