#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        #maybe use numpy next time for a better performance

        for i, (j, k) in enumerate(sorted(zip(nums, range(len(nums))), reverse=True)):

            nums[k] = str(i+1) if i > 2 else ["Gold", "Silver", "Bronze"][i] + " Medal"

        return nums

        

        # ranked_list = sorted(nums, reverse=True)


        # answer = []
        # for i in nums:

        #     answer.append(str(ranked_list.index(i)+1))

        # length = len(nums)

        # first,sec,third=False,False,False
        # for i in range(length):

        #     if answer[i] == '1':
        #         answer[i] = "Gold Medal"
        #         first=True
        #     elif answer[i] == '2':
        #         answer[i] = "Silver Medal"
        #         sec=True
        #     elif answer[i] == '3':
        #         answer[i] = "Bronze Medal"
        #         third=True

        #     if first and sec and third:

        #         break

        # return answer
