#
# @lc app=leetcode id=2120 lang=python3
#
# [2120] Execution of All Suffix Instructions Staying in a Grid
#

# @lc code=start
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = [0]*len(s)
        directions = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
        for i in range(len(s)):
            x, y = startPos
            count = 0
            for j in range(i, len(s)):
                x, y = x+directions[s[j]][0], y+directions[s[j]][1]
                if 0 <= x < n and 0 <= y < n:
                    count += 1
                else:
                    break
            ans[i] = count
        return ans

# @lc code=end
