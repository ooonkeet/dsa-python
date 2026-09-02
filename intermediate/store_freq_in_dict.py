frq_map=dict()
freq={}
nums1=[5,6,7,7,1,9,111,1,1,5,1,1]
x=int(input("Enter number to find frequency: "))
for i in range(0,len(nums1)):
    if nums1[i] in frq_map:
        frq_map[nums1[i]]+=1
    else:
        frq_map[nums1[i]]=1

for i in range(0,len(nums1)):
    freq[nums1[i]]=freq.get(nums1[i],0)+1
print("Frequency of",x,"is",frq_map[x])
print("Frequency of",x,"is",freq[x])