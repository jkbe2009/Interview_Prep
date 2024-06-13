
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        s1map, s2map = {}, {}
        s = 0

        def is_anagram(map1, map2):            
            if len(map1) != len(map2):
                return False
            
            for k, v in map1.items():
                if k not in map2 or v != map2[k]:
                    return False
            return True

            
        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1

        for e in range(len(s2)):
            s2map[s2[e]] = s2map.get(s2[e], 0) + 1

            if e-s+1 == len(s1):
                if is_anagram(s1map, s2map):
                    return True
                s2map[s2[s]] = s2map.get(s2[s]) - 1
                if s2map[s2[s]] == 0:
                    del s2map[s2[s]]
                s += 1

        return False