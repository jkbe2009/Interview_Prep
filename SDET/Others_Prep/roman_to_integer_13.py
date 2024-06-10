
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        n = len(s)
        res = 0

        for i in range(n):
            val = roman[s[i]]
            if i < n-1 and roman[s[i+1]] > val:
                res = res - val
            else:
                res = res + val

        return res