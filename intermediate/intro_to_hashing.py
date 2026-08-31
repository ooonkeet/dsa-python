n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2,7]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
        print("Number",num,"is out of range")
    else:
        print("Frequency of",num,"is",hash_list[num])