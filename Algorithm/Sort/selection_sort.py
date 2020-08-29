arr = [1,2,5,7,3,6,4]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i,len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    
    temp = arr[min_index]
    arr[min_index] = arr[i]
    arr[i] = temp

print(arr)