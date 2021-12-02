#
# @lc app=leetcode id=1196 lang=python3
#
# [1196] How Many Apples Can You Put into the Basket
#

# @lc code=start
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight.sort()
        
        current = 0
        ans = 0
        for i in weight:
            current += i
            if current > 5000:
                break
            ans+=1
        return ans
        
# @lc code=end

