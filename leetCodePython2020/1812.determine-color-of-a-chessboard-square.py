#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        s = {}
        for i in range(97, 97+8):
            s[chr(i)] = i-97+1

        return (s[coordinates[0]]+int(coordinates[1])-1) % 2 == 0


# @lc code=end
