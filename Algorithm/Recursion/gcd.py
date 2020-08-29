def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b,a%b)

print(gcd(65,15))

def count(arr,x):
    if len(arr) == 1:
        if arr[0] == x:
            return 1
        return 0
    mid = len(arr)//2
    return count(arr[:mid],x) + count(arr[mid:],x)

print(count([2,1,3,0,2,3,1,4],2))

def power(x,n):
    if n == 0:
        return 1
    return x*power(x,n-1)

print(power(2,3))


