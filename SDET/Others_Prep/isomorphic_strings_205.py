
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1, map2 = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            k = s[i]
            v = t[i]
            if k in map1 and map1[k] != v:
                return False
            map1[k] = v
            
            if v in map2 and map2[v] != k:
                return False
            map2[v] = k
        
        return True