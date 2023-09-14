# palindrome number

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)

        if x == x[::-1]:
            return 'true'
        else:
            return 'false'


solution = Solution()

test_1 = 121
test_2 = -121
test_3 = 10

print(solution.isPalindrome(-121))


