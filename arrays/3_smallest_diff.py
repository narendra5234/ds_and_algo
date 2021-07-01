# approach 1: brute force, iterate through two arrays and keep track of smallest difference.O(n2)
# approach 2: O(nlogn)

def smallest_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    l1, l2 = 0, 0
    smallest, diff = float("inf"), float("inf")
    res = []
    while l1 < len(arr1) and l2 < len(arr2):
        diff = abs(arr1[l1]-arr2[l2])
        if arr1[l1] < arr2[l2]:
            l1 += 1
        elif arr1[l1] > arr2[l2]:
            l2 += 1
        else:
            return [arr1[l1], arr2[l2]]
        if smallest > diff:
            smallest = diff
            res = [arr1[l1], arr2[l2]]
    return res
