# approach 1: can use combination of two pointers and hash table.
# approach 2: traverse through each element and apply two pointers approach

def three_number_sum(arr, target_sum):
    res = []
    arr.sort()
    for i in range(len(arr) - 2):
        l, r = i + 1, len(arr) - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s == target_sum:
                res.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
            elif s < target_sum:
                l += 1
            elif s > target_sum:
                r -= 1
    return res


print(three_number_sum([-8, -6, 1, 2, 3, 5, 6, 12], 0))
