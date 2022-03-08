#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        # Handle the case where k is 0
        if k == 0:
            return [0]*len(code)

        # Handle the case where k > 0
        else:
            a = code + code

            if k > 0:
                for i in range(len(code)):
                    code[i] = sum(a[i + 1:i + k + 1])

        # Handle the case where k < 0
            else:
                a = code + code
                for i in range(len(code)):
                    code[i] = sum(a[len(code) + i + k: len(code) + i])

        return code

# @lc code=end
