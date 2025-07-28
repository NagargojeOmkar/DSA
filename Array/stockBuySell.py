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


nums = [7, 1, 5, 3, 6]
total = 0
result = []

max_index = nums.index(max(nums))
min_index = nums.index(min(nums))


nums = [7, 4, 2, 1]

max_index = nums.index(max(nums))
min_index = nums.index(min(nums))

print("Max index:", max_index)
print("Min index:", min_index)

if min_index < max_index:
    print("✅ Profit possible (Buy first, sell later)")
elif min_index > max_index:
    print("❌ No profit (Buy comes after sell, invalid)")
else:
    print("😅 Same index, no transaction")
