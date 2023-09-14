# Search insert position

class Solution(object):
    def searchInsert(self, nums, target):
        # if in the list

        if target in nums:
            return nums.index(target)

        if target > max(nums):
            return nums.index(max(nums)) + 1

        for i in range(len(nums)):
            if target < nums[i]:
                return i


solution = Solution()

nums_1 = [1, 3, 5, 6]
target_1 = 5
# 2

nums_2 = [1, 3, 5, 6]
target_2 = 2
# 1

nums_3 = [1,3,5,6]
target_3 = 7
# 4

nums_4 = [1,3,5,6]
target_4 = 2
print(solution.searchInsert(nums_4, target_4))
