"""SUBARRAY"""

nums = [2, -5, 3, 7, -1, +5, 3, -8, -2, 6, -1, -2, 7, -6]
# n = len(nums)
# total = 0
# maxi = float("-inf")

# for i in range(0, n):
#     total = 0
#     for j in range(i, n):
#         total = total + nums[j]
#         maxi = max(maxi, total)
# print(maxi)


""" subarray """


nums = [2, -5, 3, 7, -1, +5, 3, -8, -2, 6, -1, -2, 7, -6]

n = len(nums)
total = 0
maxi = float("-inf")

for i in range(0, n):
    total = total + nums[i]
    maxi = max(maxi, total)

    if total < 0:
        total = 0

print(maxi)
