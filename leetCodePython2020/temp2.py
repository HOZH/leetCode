from collections import Counter
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = None, None
        shortestDicstance = float('inf')
        for i, word in enumerate(wordsDict):
            if word1 == word:
                if pos2 != None:
                    shortestDicstance = min(shortestDicstance, abs(pos2-i))
                pos1 = i
            elif word2 == word:
                if pos1 != None:
                    shortestDicstance = min(shortestDicstance, abs(pos1-i))
                pos2 = i
        return shortestDicstance


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in words:
                if i in j and len(i) != len(j):
                    ans.append(i)

        return set(ans)


class Solution:
    def minimumMoves(self, s: str) -> int:

        count = 0
        covered_len = 0
        for i in range(len(s)):
            current = s[i]
            if current == 'O':
                covered_len = max(0, covered_len-1)
            elif current == 'X':
                if covered_len != 0:
                    covered_len -= 1
                else:
                    count += 1
                    covered_len = 2

        return count

class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans 


class Solution:
    def longestPalindrome(self, s: str) -> int:

        counter = Counter(s)
        ans = 0
        for i in counter.values():
            ans += i//2
        ans *= 2
        if ans < len(s):
            ans += 1
        return ans
