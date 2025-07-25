"""Largest element in array"""

# nums = [55, 23, 46, 754, 755, 87, 23, 7, 34, 6543, 231, 124, 5, 344]

# Largest_num = nums[0]
# n = len(nums)

# for i in range(0, n):
#     if nums[i] > Largest_num:
#         Largest_num = nums[i]

# print(Largest_num)


# Second method
# just take -inf as largest element value

# Largest_num = float("-inf")
# n = len(nums)

# for i in range(0, n):
#     if nums[i] > Largest_num:
#         Largest_num = nums[i]

# print(Largest_num)


""" second largest element """

# largest = float("-inf")
# s_largest = float("-inf")
# n = len(nums)

# for i in range(0, n):
#     if nums[i] > largest:
#         largest = nums[i]
# print(largest)

# for i in range(0, n):
#     if nums[i] > s_largest and nums[i] != largest:
#         s_largest = nums[i]
# print(s_largest)


# APPORCH 2


# def Second_largest():

#     nums = [2, 3, 5543, 342, 323, 4235, 435634, 5234523, 35]
#     largest = float("-inf")
#     Sec_largest = float("-inf")
#     n = len(nums)

#     for i in range(0, n):
#         if nums[i] > largest:
#             Sec_largest = largest
#             largest = nums[i]
#         elif nums[i] > Sec_largest and nums[i] != largest:
#             Second_largest = nums[i]

#     return Sec_largest


# ans = Second_largest()
# print(ans)


# def Second_largest():
#     nums = [2, 3, 5543, 342, 323, 4235, 435634, 5234523, 35]
#     largest = float("-inf")
#     Sec_largest = float("-inf")
#     n = len(nums)

#     for i in range(0, n):
#         if nums[i] > largest:
#             Sec_largest = largest
#             largest = nums[i]
#         elif nums[i] > Sec_largest and nums[i] != largest:
#             Sec_largest = nums[i]

#     return Sec_largest  # return should be outside the loop


# ans = Second_largest()
# print(ans)


""" Third Largest Element """


# def thirdMax(nums):
#     first = float("-inf")
#     second = float("-inf")
#     third = float("-inf")
#     n = len(nums)

#     for i in range(0, n):
#         if nums[i] > first:
#             third = second
#             second = first
#             first = nums[i]
#         elif nums[i] > second and nums[i] != first:
#             third = second
#             second = nums[i]
#         elif nums[i] > third and nums[i] != first and nums[i] != second:
#             third = nums[i]

#     if third == float("-inf"):
#         return first
#     return third


# nums = [3, 2, 1]
# print(thirdMax(nums))


def findNonMinOrMax(nums):
    maxx = float("-inf")
    minn = float("-inf")
    n = len(nums)

    for i in range(0, n):
        if nums[i] > maxx:
            maxx = nums[i]
            return maxx
    for i in range(0, n):
        if nums[i] < minn:
            minn = nums[i]
            return minn


nums = [3, 4, 5]
print(findNonMinOrMax(nums))
