#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            ans.append(ans[-1] ^ i)
        return ans


# @lc code=end
