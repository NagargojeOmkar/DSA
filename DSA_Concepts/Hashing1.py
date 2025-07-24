# """Most Frequent Character"""

# s = "ababcbacadefegdehijhklij"

# hashList = dict()


# for char in s:
#     ascii_value = ord(char)
#     index = ascii_value - 97
#     if index in hashList:
#         hashList[index] += 1
#     else:
#         hashList[index] = 1

# max_freq = -1
# max_char = ""

# for index in s:
#     if hashList[index] > max_freq:
#         max_freq = hashList[index]
#         max_char = hashList[chr(index)]

# print(max_char)
# print(max_freq)


s = "hellopythonprogramming"

hashList = dict()

for char in s:
    if char in hashList:
        hashList[char] += 1
    else:
        hashList[char] = 1
print(hashList)

max_freq1 = -1
max_freq2 = -1
max_char = ""
max_char = ""
