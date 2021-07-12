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

        def c(nums, target_count, depth, start_index, current_list, ans):

            if target_count == depth:
                # ans.append(current_list)
                ans.append(current_list[:])
                return

            for i in range(start_index, len(nums)):
                # c(nums,target_count,depth+1,i+1,current_list+[nums[i]],ans)

                current_list.append(nums[i])
                c(nums, target_count, depth+1, i+1, current_list, ans)
                current_list.pop()

        self.ans = []
        c([i for i in range(1, n+1)], k, 0, 0, [], self.ans)

        return self.ans

# @lc code=end
