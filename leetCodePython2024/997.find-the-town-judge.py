#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) == 0:
            return 1 if n == 1 else -1
        # 2023 revision

        be_trusted, trust_others = [
            0 for _ in range(n+1)], [0 for _ in range(n+1)]
        for i, j in trust:
            be_trusted[j] += 1
            trust_others[i] += 1
        for i in range(1, n+1):
            if be_trusted[i] == n-1:
                if trust_others[i] == 0:
                    return i
                else:
                    continue
        return -1


# @lc code=end
