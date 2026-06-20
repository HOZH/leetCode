#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:


# 1, 3, 5 , 7
curr = 1, 3
next = 3, 5


[3,6,9,1] -> [1,3,6,9]
curr = 3 | 6 | 9
next = 6 | 9 | 1




output = 3
if next > curr:
    output = max(curr + next, output)


[6, 9,8,]
[6,8,9]



# bag = {1:1, 3:1, 5:1, 7:1}
# bag.keys() = 1,3,5,7 | 7,3,1,5
        
        
# @lc code=end

