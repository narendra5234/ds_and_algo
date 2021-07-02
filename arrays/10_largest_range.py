# approach 1: use sort O(nlogn)
def largest_range(arr):
    arr.sort()
    longest_range = 1
    current_range = 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]-1:
            current_range += 1
        else:
            longest_range = max(longest_range, current_range)
            current_range = 1
    return max(longest_range, current_range)
# approach 2: implement using O(n)




