nums = [
    1,
    2,
    5,
    3232,
    4,
    21,
    1,
    2,
    3,
    4,
    5,
    8,
    5,
    6,
    3,
    2,
    1,
    5,
    6,
    3,
    2,
    46,
    3,
    2,
    5,
    6,
    2,
    8,
    5,
    6,
    8,
    8,
]


my_dict = {}


for i in range(len(nums)):
    if nums[i] in my_dict:
        my_dict[nums[i]] += 1
    else:
        my_dict[nums[i]] = 1
print(my_dict)
