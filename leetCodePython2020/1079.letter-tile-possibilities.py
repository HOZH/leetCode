#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        res = set()
        
        @lru_cache(None)
        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i] + t[i+1:])

        dfs('', tiles)
        return len(res)

# @lc code=end
