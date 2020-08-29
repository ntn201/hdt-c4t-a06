def coin_change(arr,n,choose=[]):
    if n == 0:
        print(choose)
    if n > 0:
        for i in arr:
            coin_change(arr,n-i,choose+[i])


arr = [1,2,5,10]
coin_change(arr,10)