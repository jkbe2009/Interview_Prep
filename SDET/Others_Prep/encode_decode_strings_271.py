
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        temp = ""
        i = 0
        
        while i < len(s):
            if s[i] == '#':
                l = int(temp)
                start = i+1
                end = start+l
                res.append(s[start:end])
                i = end
                temp = ""
            else:
                temp += s[i]
                i += 1
                
        return res

    """
    def encode(self, strs):
        # write your code here
        res = ''
        for s in strs:
            code = str(len(s))+'#'
            res = res + code + s
        return res
    """
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    """
    def decode(self, str):
        # write your code here
        res = []
        temp = ''
        flag = True
        s = 0
        l = -1
        i = 0   

        while i < len(str):
            if str[i] == '#' and flag:
                print(temp)
                l = int(temp)
                s = i+1
                flag = False
                temp = ''
            elif i == s+l:
                res.append(temp)
                flag = True
                s, l = 0, -1
                temp = ''
                continue
            else:
                temp = temp + str[i]
            i += 1
        
        res.append(temp)
        return res
    """

