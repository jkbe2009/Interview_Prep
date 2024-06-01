
class MinStack(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.st1.append(val)
        if len(self.st2) == 0 or val <= self.st2[-1]:
            self.st2.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.st1.pop()
        if len(self.st2) > 0 and val == self.st2[-1]:
            self.st2.pop()
        return val
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.st1) == 0:
            return -1
        return self.st1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.st2) == 0:
            return -1
        return self.st2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()