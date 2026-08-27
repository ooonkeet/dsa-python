from math import *
def count(num):
    return int(log10(num)+1)
n=int(input("Enter number: "))
print("Number of digits in",n,"is",count(n))