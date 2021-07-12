#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # if len(nums) == 0:
        #     return [[]]

        # self.ans = []

        # def helper(current, lis):

        #     if len(lis) == 1:
        #         self.ans.append(current+[lis[0]])
        #         return

        #     for i in lis:
        #         index = lis.index(i)
        #         helper(current+[i], lis[:index]+lis[index+1:])

        # helper([], nums)
        # return self.ans

        self.ans = []

        def p(nums, target_count, depth, used, current_list):
            if depth == target_count:
                # self.ans.append(current_list[:])
                self.ans.append(current_list)

                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                # current_list.append(nums[i])
                p(nums, target_count, depth+1, used, current_list+[nums[i]])
                # p(nums, target_count, depth+1, used, current_list)

                # current_list.pop()
                used[i] = False

        p(nums, len(nums), 0, [False]*len(nums), [])
        return self.ans


# @lc code=end
