'''
power set
nums=[1,2,3]
2   1   0
----------
0   0   0  -> []
0   0   1  -> [1]
0   1   0  -> [2]
0   1   1  -> [1,2]
1   0   0  -> [3]
1   0   1  -> [1,3]
1   1   0  -> [2,3]
1   1   1  -> [1,2,3]

N = 3 -> 2^3=8(2^N)

tc = O(N*2^N)
sc = O(2^N*N)

'''

n=int(input("Enter length of list = "))
nums=[]
for i in range(n):
    val=input("Enter value = ")
    nums.append(val)
tot=1<<n
res=[]
for num in range(0,tot):
    lst=[]
    for i in range(0,n):
        if num & (1<<i)!=0:
            lst.append(nums[i])
    res.append(lst)
print("Total subsets are =",res)