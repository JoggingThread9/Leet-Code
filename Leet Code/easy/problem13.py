# roman numeral to integer

class Solution(object):
    def __init__(self):
        self.num = None
        self.input = None

        self.numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        self.num = 0
        self.input = s

        if 'IV' in self.input:
            self.num -= 6
            self.num += 4

        if 'IX' in self.input:
            self.num -= 11
            self.num += 9

        if 'XL' in self.input:
            self.num -= 50
            self.num += 40

        if 'XC' in self.input:
            self.num -= 60
            self.num += 40

        if 'CD' in self.input:
            self.num -= 600
            self.num += 400

        if 'CM' in self.input:
            self.num -= 1100
            self.num += 900

        for i in range(len(self.input)):
            self.num += self.numerals[self.input[i]]

        return self.num

solution = Solution()
test = ["III", "LVIII", "MCMXCIV"]

for i in test:
    print(solution.romanToInt(i))




