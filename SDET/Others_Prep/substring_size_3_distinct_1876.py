class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window technique
        occ = 0
        st = 0
        bag = {}

        for e in range(len(s)):
            bag[s[e]] = bag.get(s[e], 0) + 1
            while st <= e and (e-st+1) >= 3:
                if len(bag) == 3:
                    occ += 1
                
                if bag[s[st]] == 1:
                    del bag[s[st]]
                else:
                    bag[s[st]] = bag[s[st]] - 1

                st = st+1
        return occ