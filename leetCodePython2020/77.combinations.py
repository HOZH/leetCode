#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# @lc code=start


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        self.ans = []
        self.target_count = k

        def c(nums, depth, start_index, current_list):

            if depth == self.target_count:
                # ans.append(current_list)
                self.ans.append(current_list[:])
                return

            for i in range(start_index, len(nums)):
                # c(nums,target_count,depth+1,i+1,current_list+[nums[i]],ans)

                current_list.append(nums[i])
                c(nums, depth+1, i+1, current_list)
                current_list.pop()

        c([i for i in range(1, n+1)], 0, 0, [])

        return self.ans

# @lc code=end
