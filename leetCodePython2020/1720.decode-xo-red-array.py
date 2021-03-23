#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        ori = [first]
        current = first

        for i in encoded:
            current ^= i
            ori.append(current)

        return ori


# @lc code=end
