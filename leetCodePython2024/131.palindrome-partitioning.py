#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def helper(sub):
            if not len(sub):
                return []
            if len(sub) == 1:
                return ((sub,),)
            ans = []
            for i in range(1, len(sub)+1):
                left, right = sub[:i], sub[i:]
                if left == left[::-1]:
                    if len(right) == 0:
                        ans.append((left,))
                        continue
                    sub_list = helper(right)
                    for j in sub_list:
                        ans.append((left,) + j)
            return tuple(ans)

        return helper(s)
# @lc code=end

