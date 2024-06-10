
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wdict = set(wordDict)
        false_result = set()

        def helper_recursive(st):
            # Base case:
            if st in wdict or st == "":
                return True
            if st in false_result:
                return False

            # Recursive case:
            for i in range(len(st)):
                if st[:i+1] in wdict:
                    if helper_recursive(st[i+1:]):
                        return True
            false_result.add(st)
            return False

        return helper_recursive(s)
        