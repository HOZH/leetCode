#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # self.ans = []
        # candidates = sorted(nums)

        # def c(nums, depth, start_index, current_list,k):
        #     if depth == k:
        #         self.ans.append(current_list[:])
        #         return

        #     for i in range(start_index, len(nums)):
        #         current_list.append(nums[i])
        #         c(nums, depth+1, i+1, current_list,k)
        #         current_list.pop()
        
        # for i in range(len(nums)+1):
        #     c(candidates, 0, 0, [], i)
        # return self.ans

        for i in range(2**len(nums)):
            current = []
            for j in range(len(nums)):
                if i & (1 << j):
                    current.append(nums[j])
            ans.append(current)


        return ans

# @lc code=end
