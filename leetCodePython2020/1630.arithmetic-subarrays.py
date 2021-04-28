#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        temp = []
        for i in range(len(l)):
            p=nums[l[i]:r[i]+1]
            p.sort()
            flag=True
            for i in range(2,len(p)):
                if p[i-1]-p[i-2]!=p[i]-p[i-1]:
                    flag=False
            temp.append(flag)
        return(temp)
        
# @lc code=end

