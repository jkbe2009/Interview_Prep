
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def without_sorting():
            if strs == None:
                return []

            if len(strs) <= 1:
                return [strs]
            
            res = {}

            for s in strs:
                count = [0] * 256
                for char in s:
                    count[ord(char)] += 1
                
                # key = tuple(count)
                key = ''
                for i, val in enumerate(count):
                    if val != 0:
                        key = key + str(chr(i)) + str(val)     

                res.setdefault(key, []).append(s)

            return res.values()

        def using_sorting():
            # Edge case:
            if strs is None:
                return []

            str_map = {}

            for s in strs:
                str_key = tuple(sorted(s))
                if str_key in str_map:
                    str_map[str_key].append(s)
                else:
                    str_map[str_key] = [s]
            
            result = [val for val in str_map.values()]

            return result
        
        # return using_sorting()
        return without_sorting()