def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        # Partition index: arr[pi] is at the correct sorted position
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Verification
nums = [10, 80, 30, 90, 40, 50, 70]
quick_sort(nums, 0, len(nums) - 1)
print("Sorted Array (Quick Sort):", nums)