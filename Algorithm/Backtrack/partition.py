def partition(arr,i=1,left=None,right=[]):
      if left == None:
    left = [arr[0]]
  if i == len(arr):
    if sum(left) == sum(right):
      print(left,right)
  if i < len(arr):
    partition(arr,i+1,left+[arr[i]],right)
    partition(arr,i+1,left,right+[arr[i]])

partition([1,2,3,5,6,5])