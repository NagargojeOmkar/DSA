
""" 1. MERGING OF AN ARRAY """


def merge_array(left, right):
    i, j = 0, 0
    n, m = len(left), len(right)
    result = []

    while i < n and j < m:

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result


"""

MERGE SORT OF AN ARRAY

"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_array(left, right)


arr = [2, 5, 6, 8, 4, 6, 3, 5, 6, 8, 35, 6879, 545, 465]

sorted = merge_sort(arr)
print(sorted)
