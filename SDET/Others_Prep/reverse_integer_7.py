
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False

        if x < 0:
            negative = True
            x = -x

        res = 0

        while x:
            digit = x % 10
            res = (res * 10) + digit
            x = x / 10

        if res > math.pow(2, 31):
            return 0

        return -res if negative else res
