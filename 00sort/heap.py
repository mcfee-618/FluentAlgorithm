import math


def heapSort(arr):
    constuct_heapify(arr)
    max_len = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_len -=1
        heapify(arr, 0,max_len)


def constuct_heapify(arr):
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i,len(arr))


def heapify(arr, i,size):
    left, right = i * 2 + 1, i * 2 + 2
    if i>= size or left >= size:
        return
    max_index = left
    if right < size and arr[right] > arr[max_index]:
        max_index = right
    if arr[i] > arr[max_index]:
        return
    arr[i], arr[max_index] = arr[max_index], arr[i]
    heapify(arr, max_index,size)



nums = [99, 3, 4, 12, -1, 8, 100, -2999]
heapSort(nums)
print(nums)