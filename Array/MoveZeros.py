# nums = [0, 1, 0, 3, 12]
# n = len(nums)
# myList = []
# zeros = 0

# for i in range(0, n):
#     if nums[i] == 0:
#         zeros += 1

#     elif nums[i] != 0:
#         myList.append(nums[i])

# Final = myList + [0] * zeros

# print(Final)


"""move zeros at end in arr"""

nums = [11, 28, 5, 60, 1, 20, 0, 1, 5, 0, 2, 0, 3, 6, 0, 0, 0]


def reverse(nums):
    if len(nums) == 1:
        return
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
        if i == len(nums):
            return
        j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        j += 1


reverse(nums)
print(nums)
