#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#

# @lc code=start
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(None)
        def helper(l, r, k):

            # l starting index, r ending index, k how many boxes after r
            # has same value as boxes[r]

            if l > r:
                return 0

            # loop through the current interval and skip the redundant
            # potential function calls
            while l < r:
                if boxes[r-1] == boxes[r]:
                    r -= 1
                    k += 1
                else:
                    break

            # base case ->eliminate the ending boxes first
            res = helper(l, r-1, 0)+(k+1)**2

            for i in range(l, r):
                # only in this case, we can cancatnate the helper(l,i) with ending k's
                if boxes[i] == boxes[r]:
                    # skip current i if boxes[i+1] has the same value as boxes[i]
                    if boxes[i] != (float('inf') if i+1 >= r else boxes[i+1]):
                        res = max(res, helper(l, i, k+1)+helper(i+1, r-1, 0))
            return res
        return helper(0, len(boxes)-1, 0)
        
# @lc code=end

