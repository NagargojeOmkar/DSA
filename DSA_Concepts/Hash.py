# list1 = [2, 5, 6, 3, 5, 2, 6, 4, 8, 7, 8, 10, 0, 2, 5, 9, 8, 7, 5]
# list2 = [
#     1,
#     5,
#     8,
#     9,
#     6,
#     3,
#     2,
#     4,
#     5,
#     7,
#     98,
#     5,
#     6,
#     136,
# ]


# count_dict = {}
# count = 0

# """ for list 1 """

# for num in list1:
#     count = 0
#     for x in list2:
#         if x == num:
#             count += 1
# print(count_dict)


s = "asghauwvajkahsjkjdajbsdnmasbasd"

q = ["a", "g", "h", "v", "d", "s", "d"]

hashList = dict()

for char in s:
    ascii_value = ord(char)
    index = ascii_value - 97
    if index in hashList:
        hashList[index] += 1
    else:
        hashList[index] = 1
print(hashList)

for char in q:
    ascii_value = ord(char)
    index = ascii_value - 97
    print(hashList[index])
