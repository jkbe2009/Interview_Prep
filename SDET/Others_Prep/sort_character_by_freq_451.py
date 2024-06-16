
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        freq = {}
        n = len(s)
        max_v = 0
        res = ""

        for c in s:
            freq[c] = freq.get(c, 0) + 1
            max_v = max(max_v, freq[c])
        
        bucket = [[] for _ in range(max_v+1)]

        for k, v in freq.items():
            bucket[v].append(k)

        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for item in bucket[i]:
                        res = res + (item * i)
        
        return res

