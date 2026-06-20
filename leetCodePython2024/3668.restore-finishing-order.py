#
# @lc app=leetcode id=3668 lang=python3
#
# [3668] Restore Finishing Order
#

# @lc code=start
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_set = set(friends)
        return [x for x in order if x in friend_set]

        ans = []
        for i in order:
            if i in friend_set:
                ans.append(i)

        return ans

# @lc code=end
