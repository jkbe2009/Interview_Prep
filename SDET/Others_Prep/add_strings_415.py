
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        res = ""

        while i >= 0 or j >= 0:
            op1 = int(num1[i]) if i >= 0 else 0 
            op2 = int(num2[j]) if j >= 0 else 0
            add = op1 + op2 + carry
            carry = 0
            if add > 9 :
                carry = add / 10
                add = add % 10
            res = str(add) + res
            i -= 1
            j -= 1
        
        if carry:
            res = str(carry) + res

        return res