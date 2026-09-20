def mini(start,goal):
    ans=start^goal
    count=0
    for i in range(0,32):
        if ans & (1<<i)!=0:
            count+=1
    return count
a=int(input("Enter source = "))
b=int(input("Enter destination = "))
print("Number of bit flips are =",mini(a,b))

# tc -> o(log2n)
# sc -> o(1)