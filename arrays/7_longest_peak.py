def longest_peak(arr):
    longest = 0
    i = 1
    while i < len(arr) - 1:
        is_peak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
        if not is_peak:
            i += 1
            continue
        l = i - 2
        while l >= 0 and arr[l] < arr[l + 1]:
            l -= 1
        r = i + 2
        while r < len(arr) and arr[r] < arr[r - 1]:
            r += 1
        peak_len = r-l-1
        longest = max(longest, peak_len)
    return longest
