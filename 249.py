from collections import defaultdict

# Runtime: O(n + m)
# Space: O(n)
# n = number of strings
# m = number of characters
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strings:
            key = self.genKey(string)
            groups[key].append(string)
        answer = []
        for string_list in groups.values():
            answer.append(string_list)
        return answer

    def genKey(self, string: str) -> str:
        if len(string) == 0:
            return ""
        delta = ord(string[0]) - ord('a')
        int_format = []
        for c in string:
            value = ord('a') + ((ord(c) - delta) % 26)
            int_format.append(chr(value))
        return ''.join(int_format)
        

'''
Plan:
Convert to a common format
like abc = 123
bcd = 234 = 123
convert to numbers
shift the sequence until all numbers are 1
create a map of common format to list of strings
return the lists from that map

How to convert to a common format?
Let's use 0 based common format
ord('a') = some number
h = 81
ord('h') - ord('a') = 8
convert a to 0
convert z to 0
ord z - ord a = z in base 0 format
that's easy

now converting the other numbers is harder
just mod 26 them

How to ensure that 012 is not truncated to 12?
just add 1 to the beginning?
or keep them as strings?
keep them as strings

let's not convert them to 0 base
ord('h') = something like 104
delta = ord h - ord a = 8

new_char = ord a + (ord old char - delta) mod 26?
'''