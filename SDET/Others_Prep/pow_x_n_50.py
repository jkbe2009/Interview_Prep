
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def iterative(x, n):
            if n == 1:
                return x
            res = 1
            for _ in range(n):
                res *= x 
            return res

        def recursive(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            return x * recursive(x, n-1)

        def recursive_opt(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            v = recursive_opt(x, n/2)

            if n % 2 == 0:
                return v*v
            else:
                return v*v*x

        
        if n == 0:
            return 1
        
        if n < 0:
            # return 1/iterative(x, -n)
            # return 1/recursive(x, -n)
            return 1/recursive_opt(x, -n)
        else:
            # return iterative(x, n)
            # return recursive(x, n)
            return recursive_opt(x, n)