def kylie(lef,rig,N):
    if lef>=rig:
        return
    N[lef],N[rig]=N[rig],N[lef]
    kylie(lef+1,rig-1,N)
b=int(input("Enter length of array: "))
K=[]*b
for i in range(b):
    K.append(int(input("Enter element: ")))
kylie(0,b-1,K)
print("Reversed array is: ",K)

# example of parameterized recursion to reverse an array
# time complexity - O(N) and space complexity - O(N) 