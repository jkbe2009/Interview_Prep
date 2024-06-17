
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        l, r = 0, len(tokens)-1
        score = 0
        max_score = 0

        while l <= r:
            if power >= tokens[l]:
                # Playing Face-up from the left token
                power -= tokens[l]
                score += 1
                max_score = max(max_score, score)
                l += 1
            elif score > 0:
                # Playing Face-down from the right token
                power += tokens[r]
                score -= 1
                max_score = max(max_score, score)
                r -= 1
            else:
                break
        
        return max_score