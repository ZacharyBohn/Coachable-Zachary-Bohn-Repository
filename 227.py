'''
Runtime: O(n)
Space: O(n)
'''
class Solution:
    def calculate(self, s: str) -> int:
        # remove white space
        s = s.replace(' ', '')
        # generate token list
        tokens = []
        token = 0
        oper = '+'
        for c in s + '+':
            if c.isdigit():
                token *= 10
                token += int(c)
            else:
                if oper == '+':
                    tokens.append(token)
                elif oper == '-':
                    tokens.append(-token)
                elif oper == '*':
                    tokens[-1] *= token
                elif oper == '/':
                    tokens[-1] = int(tokens[-1] / token)
                else:
                    raise Exception(f'Unknown char: {c}')
                token = 0
                oper = c
        return sum(tokens)