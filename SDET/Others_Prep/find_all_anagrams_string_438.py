
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        st = 0
        smap, pmap = {}, {}
        res = []

        def is_same(map1, map2):
            return map1 == map2

        for ch in p:
            pmap[ch] = pmap.get(ch, 0) + 1

        for e in range(len(s)):
            smap[s[e]] = smap.get(s[e], 0) + 1

            if e-st+1 == len(p):
                if is_same(pmap,smap):
                    res.append(st)
                smap[s[st]] = smap.get(s[st]) - 1
                if smap[s[st]] == 0:
                    del smap[s[st]]
                st += 1
        
        return res
            
