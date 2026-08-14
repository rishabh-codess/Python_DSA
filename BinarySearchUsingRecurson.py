def BinarySearchHealper(ll, x, s, e):
    # Base Case: element not found
    if s > e:
        return False

    # Find middle index
    m = s + (e - s) // 2

    # Case 1: Found target
    if ll[m] == x:
        return True

    # Case 2: Target is in the right half
    elif x > ll[m]:
        return BinarySearchHealper(ll, x, m + 1, e)

    # Case 3: Target is in the left half
    else:
        return BinarySearchHealper(ll, x, s, m - 1)


def BinarySearch(ll, x):
    # Call the helper with starting bounds: s = 0, e = len(ll) - 1
    return BinarySearchHealper(ll, x, 0, len(ll) - 1)


# Test
print(BinarySearch([1, 2, 3, 4, 5, 6, 7], 5))  # Output: True
