#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count, allowed = 0, set([*allowed])

        for word in words:
            flag = True
            for ch in word:

                if ch not in allowed:
                    flag = False
                    break
            if flag:
                count+=1
        return count
            

        
# @lc code=end

