
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
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
                if len(min_heap) >= k and item < min_heap[0]:
                    continue
                heapq.heappush(min_heap, item)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
            
            return heapq.heappop(min_heap)

        # return option_1()
        return option_2()

