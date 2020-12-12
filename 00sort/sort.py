import copy

# 选择排序
def select_sort(nums):
    for i in range(len(nums) - 1):
        value = nums[i]
        index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < value:
                value = nums[j]
                index = j
        nums[i], nums[index] = nums[index], nums[i]

    return nums

# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        for j in range(i, 0, -1):
            if nums[j] > nums[j - 1]:
                break
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums

# 归并排序
def combine_sort(nums, l, r):
    if l >= r:
        return
    mid = int(l + (r - l) / 2)
    combine_sort(nums, l, mid)
    combine_sort(nums, mid + 1, r)
    values = copy.deepcopy(nums)
    index_l, index_r, index = l, mid + 1, l
    # merge two sorted array
    while index_l <= mid and index_r <= r:
        if values[index_l] < values[index_r]:
            nums[index] = values[index_l]
            index_l += 1
        else:
            nums[index] = values[index_r]
            index_r += 1
        index += 1
    if index_l <= mid:
        start, end = index_l, mid
    else:
        start, end = index_r, r

    while start <= end:
        nums[index] = values[start]
        start += 1
        index += 1


# 快速排序
def quick_sort(nums,l,r):
    left,right = l,r
    if l>=r :
        return
    value = nums[l]
    while l<r:
        while l<r and nums[r]> value:
            r-=1
        nums[l] = nums[r]
        while l<r and nums[l]< value:
            l+=1
        nums[r] = nums[l]
    nums[r] = value
    quick_sort(nums,left,l)
    quick_sort(nums,l+1,right)

# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    
    
        
    

nums = [99, 3, 4, 12, -1, 8, 100, -2999]
#print(insert_sort(nums))
#print(select_sort(nums))
#combine_sort(nums,0,len(nums)-1)
#quick_sort(nums,0,len(nums)-1)
bubble_sort(nums)
print(nums)
