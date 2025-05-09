from collections import defaultdict
from string import ascii_lowercase

# Runtime: O(n)
# Space: O(n)
# n = number of characters in strings
#
# Time to complete: 35:00
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strings:
            key = self.genKey(string)
            groups[key].append(string)
        answer = []
        for key,item in groups.items():
            answer.append(item)
        return answer
    
    def genKey(self, string: str) -> str:
        delta = ord(string[0])
        uniform = []
        for c in string:
            i = (ord(c) - delta) % 26
            uniform.append(ascii_lowercase[i])
        return ''.join(uniform)

'''
Can think of the problem as numbers instead of letters.
should make things a bit simpler.

abc -> 1,2,3

Need a uniform standard that all string can fit into.
abc -> 1,2,3
xyz -> 24,25,26 -> 1,2,3

Since the window can slide, a standard could be:
differences between characters
abc -> null, +1, +1
xyz -> null, +1, +1

But we need to store the standard representation of the strings
in a way that we can hash it, since we will be using a hashmap
in order to compare matches in O(1) time.

could make the first letter always a, then adjust the other letters
to be valid for that string.
abc -> abc
xyz -> abc
fhi -> acd

using that as a key will be easy.

ok, so we need a function to convert a string to the common
string format
then we loop through the given strings, and keep placing
them into a hashmap using that given string as a key.
can use a defaultdict
loop through the hashmap to create a list.

a = 97
f = 97 - 97 = 0 

bcd
 98 99 100
-97 97 97
=
1 2 3

How to make sure a-z is only outputted?
use string.ascii_lowercase
'''