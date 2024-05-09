class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
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