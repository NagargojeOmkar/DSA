# def maxProfit(prices):
#     n = len(prices)
#     maxx = max(prices)
#     minn = min(prices)

#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if prices[i] > prices[j]:
#                 return 0
#             elif prices[i] < prices[j]:
#                 return maxx - minn


# prices = [2, 7, 6, 4, 3, 1]

# print(maxProfit(prices))


"""remove duplicates from sorted array"""

arr = [2, 5, 6, 3, 9, 5, 6, 3, 2, 2, 3, 6, 5, 6]
n = len(arr)
result = []

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            arr.append(arr[j])
            result.append(arr[j])
print(arr)
print(result)
