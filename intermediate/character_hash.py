s=input("Enter the string to be tallied: ")
n=int(input("Enter the number of characters to be tallied: "))
arr1=[]
for i in range(0,n):
    c=input("Enter character: ")
    arr1.append(c)
char_list=[0]*26
for char in s:
    char_list[ord(char)-97]+=1
for chr in arr1:
    print("Frequency of",chr,"is",char_list[ord(chr)-97])

# remember this is for lowercase letters only.

str=input("Enter the string to be tallied: ")
n1=int(input("Enter the number of characters to be tallied: "))
arr2=[]
hsh=[0]*26
for i in range(0,n1):
    c1=input("Enter character: ")
    arr2.append(c1)
for ch in str:
    hsh[ord(ch)-65]+=1
for chr1 in arr2:
    print("Frequency of",chr1,"is",hsh[ord(chr1)-65])

# this is for uppercase letters only.