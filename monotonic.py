#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

#Given an integer array nums, return true if the given array is monotonic, or false otherwise.

from typing import List

def isMonotonic(nums: List[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing


# test cases
if __name__ == "__main__":
    tests = [
        ([1, 2, 2, 3], True),
        ([6, 5, 4, 4], True),
        ([1, 3, 2], False)
    ]

    for nums, expected in tests:
        result = isMonotonic(nums)
        print(nums, "→", result, "| expected:", expected)
