#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        self.ans = []

        def helper(current, lis):

            if len(lis) == 1:
                self.ans.append(current+[lis[0]])
                return

            for i in lis:
                index = lis.index(i)
                helper(current+[i], lis[:index]+lis[index+1:])

        helper([], nums)
        return self.ans

# @lc code=end
