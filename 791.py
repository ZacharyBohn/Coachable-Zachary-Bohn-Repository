from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1
        answer = []
        for char in order:
            answer.append(char * char_counts[char])
        for char,count in char_counts.items():
            if char not in order:
                answer.append(char * count)
        return ''.join(answer)

'''
For a string, dab
all d's first
then all a's
then all b's
all other character will be appended to the end in any order

'''