#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, digit = coordinates[0], int(coordinates[1])
        temp = ((ord(letter)-96) % 2) == 0
        return temp if digit % 2 != 0 else not temp

# @lc code=end
