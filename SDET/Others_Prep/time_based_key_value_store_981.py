
class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        val = (timestamp, value)
        self.store.setdefault(key, []).append(val)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""

        t = timestamp
        li = self.store[key]
        # Edge cases:
        if t < li[0][0]:
            return ""
        if t > li[-1][0]:
            return li[-1][1]

        """
        # Get in O(n):
        for item in reversed(li):
            if item[0] <= t:
                return item[1]
        """

        # Get in O(logn):
        l, r = 0, len(li)-1

        while l<r:
            m = (l+r)//2

            if li[m][0] == t:
                return li[m][1]
            elif t < li[m][0]:
                r = m-1
            else:
                l = m+1
        
        return li[l][1] if li[l][0] <= t else li[l-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)