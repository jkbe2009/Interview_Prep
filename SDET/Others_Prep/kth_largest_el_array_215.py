
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = {}
        min_heap = []

        for val in nums:
            map[val] = map.get(val, 0) + 1
        
        def option_1():
            # O(n)+O(n)+O(klogn) || O(n)+O(n)
            max_heap = [-1*item for item in nums]
            heapq.heapify(max_heap)
            for i in range(k):
                val = heapq.heappop(max_heap)
                if i == k-1:
                    return -1*val

        def option_2():
            # O(n)+O(n-klogk) || O(n+k)
            min_heap = []
            for item in nums:
                heapq.heappush(min_heap, item)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
            
            return heapq.heappop(min_heap)

        # return option_1()
        return option_2()

