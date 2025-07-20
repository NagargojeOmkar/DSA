"""NUMBER THAT DIVISIBLE WITH"""

from math import sqrt

# Num = int(input("enter you number that you want to check = "))
# divList = []
# for i in range(1, Num + 1):
#     if Num % i == 0:
#         divList.append(i)
# print(divList)

""" Second Approchhh  """

# Numm = []
# result = []

# for i in range(1, (Num // 2) + 1):
#     if Num % i == 0:
#         result.append(i)
# result.append(Num)

# print(result)

""" third approch """

# result = []

# for i in range(1, int(sqrt(Num))):
#     if Num % i == 0:
#         quo = Num // i
#         result.append((i, quo))
# print(result)


""" Optimal solotion """

# num = int(input("Enter your number = "))
# result = []

# for i in range(1, int(sqrt(num)) + 1):
#     if num % i == 0:
#         result.append(i)
#     if num // i != i:
#         result.append(num // i)
# print(result)

# print(sorted(result))
