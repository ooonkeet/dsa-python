def sel_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
n=int(input("Enter length of array: "))
arr=[]*n
for i in range(n):
    arr.append(int(input("Enter element: ")))
sel_sort(arr)
print("Sorted array is: ",arr)
# time complexity - O(N^2) and space complexity - O(1)