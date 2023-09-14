# remove duplicates from sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        # cannot use another array

        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                k += 1

        count = 0

        for i in range(len(nums)):
            var = nums[i-count]

            if nums[i - count] in nums[:i-count]:
                val = nums.pop(i-count)
                nums.append(val)
                count += 1

        return k, nums


solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

print(solution.removeDuplicates(nums))

