#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        self.ans = []

        def helper(strs):

            sets = list(map(lambda x: set([*x]), strs))

            temp_matched = sets[0]

            for i in range(1, len(sets)):

                temp_matched = temp_matched & sets[i]

            if len(temp_matched) == 0:
                return

            self.ans.extend(temp_matched)

            for i in temp_matched:

                for index in range(len(strs)):
                    strs[index] = strs[index].replace(i, '', 1)

            helper(strs)

        helper(A)

        return self.ans


# @lc code=end
