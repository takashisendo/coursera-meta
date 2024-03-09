def quick_sort(arr):
    # Initialize the number of swaps to 0
    swaps = 0

    def partition(low, high):
        nonlocal swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr, swaps

# Example usage
arr = [3, 6, 8, 10, 120, 1, 2, 1,8,9,2,3,1,4]
sorted_arr, swaps = quick_sort(arr)
print(sorted_arr, swaps)
