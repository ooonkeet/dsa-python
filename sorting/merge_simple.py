def merge_array(left,right):
    res=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i<n:
        res.append(left[i])
        i+=1
    while j<m:
        res.append(right[j])
        j+=1
    return res
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    left_half=merge_sort(left)
    right_half=merge_sort(right)
    return merge_array(left_half,right_half)
n=int(input("Enter length of array: "))
arr=[]*n
for i in range(n):
    arr.append(int(input("Enter element: ")))
sorted_arr=merge_sort(arr)
print("Sorted array is: ",sorted_arr)
# time complexity - O(NlogN) and space complexity - O(N)