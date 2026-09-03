def palin(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palin(s[1:-1])
# example of simple recursion to check if a string is palindrome or not
def pal(s,lef,rig):
    if lef>=rig:
        return True
    if s[lef]!=s[rig]:
        return False
    return pal(s,lef+1,rig-1)
# example of parameterized recursion to check if a string is palindrome or not

str=input("Enter a string to check if it is palindrome or not: ")
if palin(str):
    print("String is palindrome")
else:
    print("String is not palindrome")
str2=input("Enter a string to check if it is palindrome or not: ")
if pal(str2,0,len(str2)-1):
    print("String is palindrome")
else:
    print("String is not palindrome")