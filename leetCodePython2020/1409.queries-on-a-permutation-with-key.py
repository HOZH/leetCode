#
# @lc app=leetcode id=1409 lang=python3
#
# [1409] Queries on a Permutation With Key
#

# @lc code=start


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        result = []
        for i in queries:
            result.append(p.index(i))
            p.remove(i)
            p.insert(0, i)

        return result

# @lc code=end
