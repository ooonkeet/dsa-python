a=int(input("Enter first number = "))
b=int((input("Enter second number = ")))
print("Before Swapping 'a' =",a,", 'b' =",b)
# swap using xor operators
a=a^b
b=a^b
a=a^b
print("After Swapping 'a' =",a,", 'b' =",b)

# check if i'th bit is set or not
p=int(input("Enter value to be set = "))
q=int(input("Enter bit to be set = "))
if(p&(1<<q))!=0:
    print(q,"bit is set")
else:
    print(q,"Bit is not set")
# set q'th bit in p

print(p|(1<<q))

# clear q'th bit in p

print(p & ~(1<<q))

# toggle c'th bit in d
c=int(input("Enter value to be set = "))
d=int(input("Enter bit to be set = "))
print(c ^ (1<<d))

# remove the last set bit(rightmost)
# 16 = 10000 and-> 15 = 01111
# 40 = 101000 and-> 39 = 100111
# 84 = 1010100 and-> 83 = 1010011
print(c&(c-1))
# check power of 2
# 2 -> 10
# 4 -> 100
# 8 -> 100
# 16 -> 1000
# if i remove the rightmost set bit i'll get 0
f=int(input("Enter a number to check whether power of 2 = "))
if (f&(f-1))==0:
    print(f,"is a power of 2")
else:
    print(f,"is not a power of 2")