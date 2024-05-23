
class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) || O(n)

        # Edge cases:
        if s == None or len(s) < 2 or len(s) % 2 != 0:
            return False

        st = []
        pair = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        for char in s:
            if char in pair:
                # Its an open paran
                st.append(char)
            else:
                # Its a closed paran
                if len(st) == 0:
                    # No Open paran seen before without a pair
                    return False
                top = st.pop()
                if pair[top] != char:
                    return False
        return len(st) == 0
        