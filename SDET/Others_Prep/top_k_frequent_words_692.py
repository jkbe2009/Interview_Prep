

import heapq

class heap:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return other.word < self.word
        else:
            return self.count < other.count

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        freq = {}
        res = []
        minheap = []

        for word in words:
            key = tuple(word)
            freq[key] = freq.get(key, 0) + 1
        
        for string, count in freq.items():
            val = heap(count, "".join(string)) 
            if len(minheap) < k or val > minheap[0]:
                heapq.heappush(minheap, val)
            if len(minheap) > k:
                heapq.heappop(minheap)

        while minheap:
            heap_val = heapq.heappop(minheap)
            res.append(heap_val.word)

        return reversed(res)