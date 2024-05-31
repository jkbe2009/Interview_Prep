
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op == '+':
                if len(stack)<2:
                    return 0
                stack.append(stack[-1]+stack[-2])
            elif op == 'C':
                if len(stack)<1:
                    return 0
                stack.pop()
            elif op == 'D':
                if len(stack)<1:
                    return 0
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)