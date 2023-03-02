#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = list(map(lambda x:str(x),nums))
        ans = []
        for i in temp:
            for j in i:
                ans.append(int(j))
        return ans


# @lc code=end
