def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)
    return min(min1, min2), max(max1, max2)

arr = [12, 45, 7, 23, 56, 3, 89]
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)
print("Array:", arr)
print("Minimum value:", minimum)
print("Maximum value:", maximum)