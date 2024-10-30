#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        current = first
        for i in encoded:
            temp = current ^ i
            ans.append(temp)
            current = temp

        return ans


# @lc code=end
