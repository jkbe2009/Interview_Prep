
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        result = []
        
        for val in nums:
            map[val] = map.get(val, 0) + 1

        # option 1: Sort the map and print the top k
        # O(n+nlogn) || O(n)
        def option1():
            sorted_items = sorted(map.items(), key = lambda item : item[1], reverse = True)
            for i in range(k):
                item = sorted_items[i]
                result.append(item[0])
            return result

        # option 2: Use a Max Heap and print the top k
        # O(n+n(heapify)+klogn(add to result)) || O(n+n)
        def option2():
            # max_heap = []
            # for item in map.items():
            #     val = (-1*item[1], item[0])
            #     heapq.heappush(max_heap, val)
            max_heap = [(-1*item[1], item[0]) for item in map.items()]
            heapq.heapify(max_heap)
            
            for i in range(k):
                val = heapq.heappop(max_heap)
                result.append(val[1])
            return result

        # option 3: Use a Min Heap and print the top k
        # O(n+klogk(build heap tree)+klogk(add to result)) || O(n+k)
        def option3():
            min_heap = []
            for item in map.items():
                val = (item[1], item[0])
                heapq.heappush(min_heap, val)
                while len(min_heap) > k:
                    heapq.heappop(min_heap)
            
            while min_heap:
                val = heapq.heappop(min_heap)
                result.append(val[1])
            return result


        # return option1()
        return option2()
        # return option3()