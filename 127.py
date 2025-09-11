# Runtime: O(n^2)
# Space: O(n)
# 
# Time to complete: 25:55
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque([endWord])
        visited = set([endWord])
        # word: distance from endWord
        dist = {endWord: 1}
        while q:
            curr = q.popleft()
            for word in wordList:
                if word in visited:
                    continue
                if self.one_char_off(word, curr):
                    dist[word] = dist[curr] + 1
                    q.append(word)
                    visited.add(word)
        min_dist = float('inf')
        for word in wordList:
            if self.one_char_off(word, beginWord):
                if word not in dist:
                    continue
                min_dist = min(min_dist, dist[word] + 1)
        return 0 if min_dist == float('inf') else min_dist
    
    def one_char_off(self, word, other) -> bool:
        mismatch = False
        for i in range(len(word)):
            if word[i] != other[i]:
                if not mismatch:
                    mismatch = True
                else:
                    # second mismatch
                    return False
        return mismatch

'''
Start with the end word (verify it is present)
then trace from that word to every other word, keeping track of how many
edges it takes to get there.


shortest path in an undirected, unweighted graph.

how to build edges?

could loop through the wordList and build all edges for endWord
then do the same for all neighbors nodes of that (bfs)
anyway to keep from having to keep looping through everytime?
runtime is O(n^2); n = wordList.length

steps:

queue start with endWord
use visited set
use dict word: distance to endWord
loop through wordList
if they are one letter off then
update dist
loop through the list one last time?


'''