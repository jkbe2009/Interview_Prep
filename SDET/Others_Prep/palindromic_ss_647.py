
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total_count = 0
        
        def count_ss(l ,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1     
            return count

        for i in range(len(s)):
            count1 = count_ss(i, i)
            count2 = count_ss(i, i+1)

            total_count += count1 + count2
        
        return total_count