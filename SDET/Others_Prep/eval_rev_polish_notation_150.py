
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        st = []

        for token in tokens:
            if token == '+':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1+op2)
            elif token == '-':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1-op2)
            elif token == '*':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1*op2)
            elif token == '/':
                op2 = st.pop()
                op1 = st.pop()
                quotient = int(op1/float(op2))
                st.append(quotient)
            else:
                st.append(int(token))
        
        return st.pop()
        