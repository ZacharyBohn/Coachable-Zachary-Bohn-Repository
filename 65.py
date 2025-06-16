import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # split the string into groups
        # with e or E being the delimiter
        numbers = re.split(r'[eE]', s)
        if len(numbers) > 2:
            # can only have 1 e
            return False
        if not self.isDecimal(numbers[0]):
            # number before e (or the only number)
            # must be a valid decimal
            return False
        if len(numbers) == 2:
            return self.isInteger(numbers[1])
        return True
    
    def isInteger(self, s: str) -> bool:
        # optional single + or -
        # followed by
        # digit(s)
        pattern = r'^[+-]?\d+$'
        return bool(re.match(pattern, s))
    
    def isDecimal(self, s: str) -> bool:
        # optional single + or -
        # followed by either
        # digit(s), optional period, optional more digits(s)
        # OR
        # period, digit(s)
        pattern = r'^[+-]?(\d+\.?\d*|\.\d+)$'
        return bool(re.match(pattern, s))
       
'''

split based on e or E

then for the first string

optional + or - (0 or 1)
[+-]?

then

two options

\d+[\.]? (one or more digits followed by an optional period)
[\.]?\d+ (an optional period followed by one or more digits)
^[+-]?(\d+[\.]?|[\.]?\d+)$
^ = start
$ = end

'''