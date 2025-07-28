"""REMOVE DUPLCIATES FROM ARRAY"""

# nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# n = len(nums)


# def Duplicates():

#     if n == 1:
#         return 1

#     i = 0
#     j = i + 1

#     for j in range(0, n):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#     return i + 1


# print(nums)


# print(Duplicates())


""" left rotate array by 1 """

# nums = [5, 6, 7, 89, 4, 2, 6, 5, 1]
# n = len(nums)

# temp = nums[n - 1]

# for i in range(n - 2, -1, -1):
#     nums[i + 1] = nums[i]
# nums[0] = temp

# print(nums)


""" rotate array by k """

# nums = [5, 6, 7, 89, 4, 2, 6, 1]
# n = len(nums)
# k = int(input("enter value of k = "))


# def reverse(nums, left, right):
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1


# reverse(nums, n - k, n - 1)
# reverse(nums, 0, n - k - 1)
# reverse(nums, 0, n - 1)

# print(nums)
