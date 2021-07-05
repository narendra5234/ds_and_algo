def sub_array_sort(arr):
    min_out_of_order, max_out_of_order = float("inf"), float("inf")
    for i in range(len(arr)):
        if is_out_of_order(i, arr[i], arr):
            min_out_of_order = min(min_out_of_order, arr[i])
            max_out_of_order = max(max_out_of_order, arr[i])
    if min_out_of_order == float("inf"):
        return [-1, -1]
    l, r = 0, len(arr) - 1
    while min_out_of_order >= arr[l]:
        l += 1
    while max_out_of_order <= arr[r]:
        r -= 1
    return [l, r]


def is_out_of_order(i, num, arr):
    if i == 0:
        return num > arr[i + 1]
    if i == len(arr) - 1:
        return num < arr[i - 1]
    return num > arr[i + 1] or num < arr[i - 1]
