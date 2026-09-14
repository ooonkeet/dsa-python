def part(nums,low,high):
    pivot=nums[low]
    i=low,j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick_sort(nums,low,high):
    if low<high:
        p_ind=part(nums,low,high)
        quick_sort(nums,low,p_ind-1)
        quick_sort(nums,p_ind+1,high)
n=int(input("Enter length of array: "))
arr=[]*n
for i in range(n):
    arr.append(int(input("Enter element: ")))
quick_sort(arr,0,n-1)
print("Sorted array is: ",arr)

# time complexity - O(NlogN) and space complexity - O(1)