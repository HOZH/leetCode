#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return list(filter(lambda z:z!=None,map(lambda y:y[0] if x in y[1] else None,enumerate(words))))
        
# @lc code=end

