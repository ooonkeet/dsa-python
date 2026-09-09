def bubble(arr):
    for i in range(len(arr)):
        isSwapped=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isSwapped=True
        if isSwapped==False:
            break
n=int(input("Enter length of array: "))
arr=[]*n
for i in range(n):
    arr.append(int(input("Enter element: ")))
bubble(arr)
print("Sorted array is: ",arr)

# time complexity - O(N^2) and space complexity - O(1)
            