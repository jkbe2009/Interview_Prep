
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
        s = 0
        sum = 0
        count = 0
        
        for e in range(len(arr)):
            sum += arr[e]

            while s <= e and e-s+1 >= k:
                # check for thresold
                if e-s+1 == k:
                    if (sum//k) >= threshold:
                        count += 1
                # remove element from start
                sum -= arr[s]
                s += 1
        return count
