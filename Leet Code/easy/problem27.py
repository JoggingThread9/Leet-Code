# remove element

class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in nums:
            if i != val:
                k += 1

        count = 0

        for i in range(len(nums)):
            if nums[i - count] == val:
                elem = nums.pop(i - count)
                nums.append(elem)
                count += 1

        return k, nums

solution = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

print(solution.removeElement(nums, val))
