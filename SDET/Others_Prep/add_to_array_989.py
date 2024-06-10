

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        First Attempt:
        --------------

        carry = 0
        i = len(num)-1
        res = []

        while k > 0 or i >=0:
            op2 = k % 10
            op1 = num[i] if i >=0 else 0
            val = op1 + op2 + carry
            carry = 0
            if val > 9:
                val = val % 10
                carry = 1
            res.insert(0, val)
            
            k = k / 10
            i -= 1
        
        if carry:
            res.insert(0, carry)
        
        while k > 0:
            res.insert(0, k % 10)
            k = k / 10

        return res

        """

        res = []

        for i in range(len(num)-1, -1, -1):
            k = num[i]+k
            res.insert(0, k % 10)
            k = k/10

        while k:
            res.insert(0, k % 10)
            k = k/10

        return res