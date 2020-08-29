def partition(arr):
    pivot = arr[-1]
    start = 0
    for i in range(len(arr)):
        if arr[i] <= pivot:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            start += 1
    return start-1, arr

def sort(arr):
    if len(arr) == 0:
        return arr
    else:
        mid, arr = partition(arr)
        return sort(arr[0:mid]) + [arr[mid]] + sort(arr[mid+1:])

print(sort([6,2,1,4,7,3,8,5]))
# arr = partition([6,2,1,4,7,3,8,5])[1]
# print(arr[0:4])
# print(arr[5:])