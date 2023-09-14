# valid parentheses

class Solution(object):
    def isValid(self, s):
        # Open brackets must be closed by the same type of brackets
        # Open brackets must be closed in the correct order
        # Every close bracket has a corresponding open bracket of the same type
        if len(s) == 1:
            return False

        closing = [')', '}', ']']

        open_curved = False
        open_curly = False
        open_square = False

        recent = []

        for i in s:
            if i in closing and len(recent) > 0:
                if recent[0] == '(' and i == ')':
                    recent.pop(0)
                elif recent[0] == '{' and i == '}':
                    recent.pop(0)
                elif recent[0] == '[' and i == ']':
                    recent.pop(0)
                else:
                    return False

            elif i == '(':
                recent.insert(0, '(')

            elif i == '{':
                recent.insert(0, '{')
            elif i == '[':
                recent.insert(0, '[')

            else:
                return False

        if len(recent) > 0:
            return False

        return True


solution = Solution()
test = ['()', '()[]{}', '(]', "([)]", "{[]}"]
test_2 = ["(])"]

for i in test_2:
    print(solution.isValid(i))
