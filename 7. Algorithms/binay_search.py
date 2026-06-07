def binary_search(arr, target):
    left= 0
    right= len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
sorted_array = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_array, 7))   # Output: 3
print(binary_search(sorted_array, 4))   # Output: -1