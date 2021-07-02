def four_number_sum(arr, target_sum):
    all_pairs_sum = {}
    res = []
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            s = arr[i] + arr[j]
            diff = target_sum - s
            if diff in all_pairs_sum:
                for pair in all_pairs_sum[diff]:
                    res.append(pair + [arr[i], arr[j]])
        for k in range(0, i):
            s = arr[i] + arr[k]
            if s not in all_pairs_sum:
                all_pairs_sum[s] = [[arr[k], arr[i]]]
            else:
                all_pairs_sum[s].append([arr[k], arr[i]])
