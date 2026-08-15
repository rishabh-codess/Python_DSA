def find_all_indices(arr, target, index=0, indices=None):
    if indices is None:
        indices = []

    # Base Case: Array end reached
    if index == len(arr):
        return indices

    # Accumulate index if target matches
    if arr[index] == target:
        indices.append(index)

    # Recursive Step
    return find_all_indices(arr, target, index + 1, indices)


# Testing Multi-Index Collector
numbers = [1, 4, 7, 4, 9, 4, 12]
result = find_all_indices(numbers, target=4)

print("All indices of 4:", result)  # [1, 3, 5]