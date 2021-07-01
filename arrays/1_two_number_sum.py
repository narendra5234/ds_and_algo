# approach 1 : brute force iterate over the list twice and checking if i+j=target_sum,
# t-O(n2), s-O(1)
def two_number_sum_1(arr, target_sum):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target_sum:
                return [arr[i], arr[j]]
    return []


# approach 2 : traversing through i and checking if j=target_sum-i is in set else, to store traversed i in set,
# t-O(n), s-O(n)
def two_number_sum_2(arr, target_sum):
    d = set()
    for i in arr:
        j = target_sum - i
        if j in d:
            return [i, j]
        else:
            d.add(i)
    return []


# approach 2: sort the array, then by using two pointers, use the left and right pointers inorder to get target sum.
# t-O(nlogn), s-O(1)
def two_number_sum_3(arr, target_sum):
    arr.sort()
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target_sum:
            return [arr[l], arr[r]]
        elif s < target_sum:
            l += 1
        elif s > target_sum:
            r -= 1
    return []


ans = two_number_sum_1([3, 5, -4, 8, 11, 1, -1, 6], 10)
assert sorted(ans) == sorted([11, -1])


ans = two_number_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10)
assert sorted(ans) == sorted([11, -1])

ans = two_number_sum_3([3, 5, -4, 8, 11, 1, -1, 6], 10)
assert sorted(ans) == sorted([11, -1])

print("SUCCESS")


