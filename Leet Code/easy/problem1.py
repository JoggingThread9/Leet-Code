# two sum

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    pass
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]


solution = Solution()

nums = [3, 4, 2]

target = 6

print(solution.twoSum(nums, target))

