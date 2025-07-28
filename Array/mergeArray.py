# nums1 = [5, 1, 32, 6, 59, 5, 4, 2, 6, 5, 56, 2, 65, 1, 32, 3]
# nums2 = [5, 2, 1, 5, 4, 6, 9, 5, 3, 5, 4, 6, 2, 65, 53, 3, 2]


# newNums = nums1 + nums2
# print(newNums)

# merge = []

# for i in range(0, len(newNums)):
#     if newNums[i] not in merge:
#         merge.append(newNums[i])
# print(merge)


"""Merge 2 Sorted Arrays"""

# 🔹 Sorted Array 1
nums1 = [1, 3, 3, 3, 3, 5, 7, 9, 12, 15]

# 🔹 Sorted Array 2
nums2 = [2, 1, 1, 1, 11, 4, 6, 8, 10, 14, 18]


n = len(nums1)
m = len(nums2)

i, j = 0, 0
result = []

while i < n and j < m:
    if nums1[i] <= nums2[j]:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
            i += 1
    else:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
            j += 1
while i < n:
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
        i += 1
while j < m:
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
        j += 1


print(result)
