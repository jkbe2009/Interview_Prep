
from collections import deque

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        bag = set()
        st = 0
        q = deque()
        res = set()

        for e in range(len(s)):

            q.append(s[e])

            if e-st+1 > 10:
                q.popleft()
                st += 1
            
            if e-st+1 == 10:
                dna = "".join(q)
                if dna in bag:
                    res.add(dna)
                bag.add(dna)
        
        return list(res)