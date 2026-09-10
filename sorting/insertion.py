def insert(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
n=int(input("Enter length of array: "))
arr=[]*n
for i in range(n):
    arr.append(int(input("Enter element: ")))
insert(arr)
print("Sorted array is: ",arr)

# time complexity - O(N^2) and space complexity - O(1)