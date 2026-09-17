def solve(ind,sub):
    if ind>=len(num):
        result.append(sub.copy())
        return
    sub.append(num[ind])
    solve(ind+1,sub)
    sub.pop()
    solve(ind+1,sub)
n=int(input("Enter length of list = "))
num=[]
for i in range(n):
    val=input("Enter a value = ")
    num.append(val)
result=[]
subset=[]
solve(0,subset)
print("Subsets of",num,"are",result)

# tc -> o(2^n)
# sc -> o(n) = stack space