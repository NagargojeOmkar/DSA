"""Two sum problem"""

nums = [2, 5, 6, 7, 12, 56, 85, 3, 7, 9, 4]

target = 10
n = len(nums)
hash_map = {}


def twoSUm():
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[(nums[i])] = i


print(twoSUm())
