arr = [7,4,3,1,5,2,6]

min_index = 1
for i in range(1,len(arr)):
    if arr[min_index] > arr[i]:
        min_index = i

print(min_index)