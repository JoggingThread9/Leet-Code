# longest common prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        # if
        Min = len(strs[0])

        for i in strs:
            if Min > len(i):
                Min = len(i)

        prefix = ''

        check = True

        for j in range(Min):
            letter = strs[0][j]
            for i in strs:
                if i[j] != letter:
                    check = False
            if check:
                prefix += letter
            else:
                break

        return prefix


solution = Solution()
test = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]

print(solution.longestCommonPrefix(test[0]))