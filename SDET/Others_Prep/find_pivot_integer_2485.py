
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lsum, rsum = 0, 0
        l, r = -1, n+1

        while l < r:
            if lsum == rsum:
                l += 1
                r -= 1
                lsum += l
                rsum += r
            elif lsum < rsum:
                l += 1
                lsum += l
            else:
                r -= 1
                rsum += r

        return l if l == r and lsum == rsum else -1