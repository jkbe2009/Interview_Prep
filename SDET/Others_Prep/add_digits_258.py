
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        def using_loop(num):
            res = 0

            while num > 0:
                digit = num % 10
                res += digit
                num = num / 10
                if num == 0 and res > 9:
                    num = res
                    res = 0
            return res
        

        def digital_root():
            res = num % 9
            return 9 if res == 0 else res

        return digital_root()
        # return using_loop(num)
        