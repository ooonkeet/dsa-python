n=int(input("Length of the list = "))
lis=[]
for i in range(n):
    val=int(input("Enter a number = "))
    lis.append(val)
hash_map={}
k=0
for num in lis:
    hash_map[num]=hash_map.get(num,0)+1
for key in hash_map:
    if hash_map[key]==1:
        print("Unique element =",key)
        k+=1
if k==0:
    print("No unique elements present.")
# xor way
asn=0
for num in lis:
    asn=asn^num
print("Unique element present =",asn)