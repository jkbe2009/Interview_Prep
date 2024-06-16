
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        imap = {}
        res = []
        seen = set()
        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] not in imap:
                imap[s[i]] = i

        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while res and ord(res[-1]) > ord(ch) and imap[res[-1]] > i:   
                temp = res.pop()
                seen.remove(temp)
            res.append(ch)
            seen.add(ch)
        
        return "".join(res)