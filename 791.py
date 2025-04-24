from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        answer = ''
        for char in order:
            answer += char * hashmap[char]
        for char,count in hashmap.items():
            if char not in order:
                answer += char * count
        return answer

'''
For a string, dab
all d's first
then all a's
then all b's
all other character will be appended to the end in any order

'''