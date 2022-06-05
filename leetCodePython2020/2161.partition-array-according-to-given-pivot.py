#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        smaller, greater, pivot_count = [], [], 0
        for i in nums:
            if i == pivot:
                pivot_count += 1
            elif i < pivot:
                smaller.append(i)
            else:
                greater.append(i)

        return smaller + [pivot] * pivot_count + greater

# @lc code=end
