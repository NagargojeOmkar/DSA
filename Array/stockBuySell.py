"""maximum profit"""

# nums = [7, 4, 2, 1]

# maxProfit = 0
# n = len(nums)
# resultt = []

# for i in range(0, n):
#     for j in range(i + 1, n):
#         if nums[j] - nums[i] > maxProfit:
#             maxProfit = nums[j] - nums[i]

# if maxProfit == 0:
#     print("No profit ")
# else:
#     print("profit is ", maxProfit)

# nums = [7, 1, 5, 3, 6]
# maxProfit = 0
# n = len(nums)

# for i in range(0, n):
#     for j in range(i + 1, n):
#         if nums[j] - nums[i] > maxProfit:
#             maxProfit = nums[j] - nums[i]

# if maxProfit == 0:
#     print("No profit")
# else:
#     print("Max Profit:", maxProfit)


"""time to find best but of stock"""

# nums = [7, 4, 2, 1, 10]
# maxProfit = 0

# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[j] - nums[i] > maxProfit:
#             maxProfit = nums[j] - nums[i]

# print(maxProfit)


""" optimal """

""" BEST SOLUTION """


nums = [7, 4, 2, 1, 8]

max_profit = float("-inf")
min_price = 0

for i in range(0, len(nums)):
    min_price = min(min_price, nums[i])
    max_profit = max(max_profit, nums[i] - min_price)
print(max_profit)
