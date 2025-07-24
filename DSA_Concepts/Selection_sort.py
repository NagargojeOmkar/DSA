"""Selection Sort"""

nums = [2, 4, 5, 8, 47, 23, 69, 56]


def selection_Sort():
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums


x = selection_Sort()


print(x)
