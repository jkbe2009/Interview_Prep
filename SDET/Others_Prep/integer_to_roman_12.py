
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        integer = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        res = ""
        for i in range(len(roman)-1, -1, -1):
            while(num >= integer[i]):
                res = res + roman[i]
                num = num - integer[i]
        
        return res