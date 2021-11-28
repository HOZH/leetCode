#
# @lc app=leetcode id=1213 lang=python3
#
# [1213] Intersection of Three Sorted Arrays
#

# @lc code=start
from collections import Counter
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        counter = Counter(arr1+arr2+arr3)
        ans=[]

        for item in counter:

            if counter[item]==3:
                ans.append(item)
        
        return ans

        
# @lc code=end

