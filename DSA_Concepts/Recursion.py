# # """1 to N printing without using for while loop"""


# # def func(i, n):
# #     if i > n:
# #         return
# #     print(i)
# #     func(i + 1, n)


# # func(1, 5)


# """Functional recursion"""


# def func(n):

#     if n == 1:
#         return 1
#     return n + func(n - 1)

#     print(x)


# func(10)


"""Factorial of any numnber"""

# Num = int(input("Entter any number = "))


# def fun(n):
#     if n == 1:
#         return 1
#     return n + fun(n - 1)


# result = fun(Num)

# print(result)


""" Reverse the ARRAY """
# arr = [5, 6, 7, 3, 4, 7, 8, 9, 1, 0]

# newlist = []


# def adalabdal(arr, left, right):
#     if left == right:
#         return 1
#     arr[left], arr[right] = arr[right], arr[right]
#     adalabdal(arr, left + 1, right - 1)


# adalabdal(arr, 1, 5)
# print(arr)


""" using while loop """


# arr = [5, 6, 7, 3, 4, 7, 8, 9, 1, 0]

# left = 0
# right = len(arr) - 1

# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# print(arr)


""" PALINDROME """

# s = "NITIN"


# def palin(s, left, right):
#     if left >= right:
#         return 1
#     if s[left] != s[right]:
#         return False
#     return palin(s, left + 1, right - 1)


# result = palin(s, 0, len(s) - 1)
# print(result)


# """ LOgic of FIBOOOOONACHIIII """


# def fibo(N):
#     if N == 0:
#         return 0
#     if N == 1:
#         return 1
#     return fibo(N - 1) + fibo(N - 2)


# result = fibo(10)
# print(result)
