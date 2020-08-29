def longest_subsequence(arr,i=0,choose=[]):
    if i == len(arr):
        return choose
    if i < len(arr):
        if choose == []:
            left = longest_subsequence(arr,i+1, choose + [arr[i]] )
            right = longest_subsequence(arr,i+1,choose)
            if len(left) > len(right):
                return left
            return right
        else:
            if arr[i] >= choose[-1]:
                left = longest_subsequence(arr,i+1,choose + [arr[i]])
                right = longest_subsequence(arr, i+1, choose)
                if len(left) > len(right):
                    return left
                return right
            else:
                return longest_subsequence(arr,i+1,choose)

print(longest_subsequence([6,1,5,3,4,7,8,2]))
