
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        i = 31

        while n:
            bit = n % 2
            res += bit * (2**i)
            n = n >> 1 
            i -= 1

        return res