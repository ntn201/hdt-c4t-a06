def factorial(n):
    # anchor
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibbonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)
    
arr = [2, 1, 5 ,9, 8, 7, 0 ,6 ,4, 3]

def min(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    left = min(arr[0:mid])
    right = min(arr[mid:])
    if left < right:
        return left
    else:
        return right

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    return sum(arr[0:mid]) + sum(arr[mid:])

def reverse(string):
    # anchor
    if len(string) == 1:
        return string
    return reverse(string[1:]) + string[0]
    # recursion