"""SOrting Methods....."""

""" 1. Selection Sort """


# nums = [2, 5, 9, 8, 4, 33, 65, 48, 68, 65, 45, 23, 65]


# def Selection_sort():
#     n = len(nums)
#     for i in range(0, n):
#         mid_element = i
#         for j in range(i + 1, n):
#             if nums[j] < nums[mid_element]:
#                 mid_element = j
#         nums[i], nums[mid_element] = nums[mid_element], nums[i]
#     return nums


# print(Selection_sort())


""" BUBBLE SORTING """


# nums = [2, 5, 6, 8, 3, 65, 9, 45, 65, 54]


# def bubble_sort():
#     n = len(nums)
#     for i in range(0, n):
#         index_key = i
#         for j in range(i + 1, n):
#             if nums[j] < nums[index_key]:
#                 index_key = j
#         nums[i], nums[index_key] = nums[index_key], nums[i]
#     return nums


# print(bubble_sort())
""" Haa warcha code chukicha aheeee yat bubble sort cha logic use kely dont use it """

""" BUBBLE SORT IS BELOWWWW """


# nums = [1, 2, 3]
# n = len(nums)


# def bubble_sort():
#     for i in range(n - 2, -1, -1):
#         is_swap = False
#         for j in range(0, i + 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 is_swap = True
#         if is_swap == False:
#             break
#     return nums


# print(bubble_sort())


""" INSERTION SORT """


""" Its little tricky but easy as well """


# nums = [2, 4, 5, 6, 9, 8, 7, 32, 87, 225, 365, 489, 654, 559, 56, 59, 87, 58, 23, 96]
# n = len(nums)


# def insertion_sort():
#     for i in range(0, n):
#         key = nums[i]
#         j = i - 1

#         while j >= 0 and nums[j] > key:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = key
#     return nums


# print(insertion_sort())


""" MERGE SOrt """

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
