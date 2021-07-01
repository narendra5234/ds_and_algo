def is_monotonic(arr):
    if len(arr) <= 2:
        return True

    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i - 1]
            continue
        diff = arr[i] - arr[i - 1]
        if (direction > 0 and diff < 0) or (direction < 0 and diff > 0):
            return False
    return True


def is_monotonic_1(arr):
    is_non_dec = True
    is_non_inc = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            is_non_dec = False
        if arr[i] > arr[i - 1]:
            is_non_inc = False
    return is_non_inc or is_non_dec


print(is_monotonic([1, 1, 1, 2, 1]))
