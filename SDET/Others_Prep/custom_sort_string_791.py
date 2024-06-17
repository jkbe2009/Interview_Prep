
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        smap = {}
        res = ""

        for ch in s:
            smap[ch] = smap.get(ch, 0) + 1
        
        for ch in order:
            if ch in smap:
                res = res + (ch *smap[ch])
                del smap[ch]
        
        for k, v in smap.items():
            res = res + (k * v)

        return res