def max_sum_subarray_with_indices(arr, k):
    if not arr or k > len(arr):
        return -1, []
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    start_index = 0
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
            start_index = i - k + 1
    
    return max_sum, arr[start_index:start_index + k]

# Test
arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum, subarray = max_sum_subarray_with_indices(arr, k)
print(f"Maximum sum: {max_sum}, Subarray: {subarray}")  # Output: 9, [5, 1, 3]