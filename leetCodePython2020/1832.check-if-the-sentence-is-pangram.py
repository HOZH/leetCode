#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        filtered = set(list(filter(lambda x: x.isalpha(), [*sentence])))

        return len(filtered) == 26

# @lc code=end
