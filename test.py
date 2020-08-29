arr =  [5,3,1,2,0,4,6]
 
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] > arr[j+i]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
 
print(arr)
