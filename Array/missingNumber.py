# nums = [1, 0, 3, 4]
# n = len(nums)
# total = 5
# Result = []

# for i in range(0, total):
#     Result.append(i)
#     if Result[i] not in nums:
#         print(Result[i])


"""missing nnuber"""

# nums = [1, 0, 3, 4]
# n = 4  # 4

# expected_sum = n * (n + 1) // 2
# actual_sum = sum(nums)

# missing = expected_sum - actual_sum
# print("Missing number is:", missing)


""" CONSECUTIVE ONE COUNT """


# nums = [1, 1, 0, 0, 4, 1, 1, 1, 1, 5, 9, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0]
# count = 0
# maxcount = 0

# for i in range(0, len(nums)):
#     if nums[i] == 1:
#         count += 1
#     else:
#         maxcount = max(count, maxcount)
#         count = 0
# print(max(count, maxcount))

""" two sum """

nums = [5, 9, 1, 2, 4, 15, 6, 3]


def twoSum():
    target = 13

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


print(twoSum())
