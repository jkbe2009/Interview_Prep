
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        res = []
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            carry = 0
            if val > 9:
                carry = 1
                val = 0
            res.append(val)
        
        if carry:
            res.append(carry)

        return res[::-1]