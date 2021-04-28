#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        graph = list(map(lambda x: set(x), graph))
        target = len(graph)-1
        ans = []

        def helper(current_seq):

            if current_seq[0] == 0:
                ans.append(current_seq)
                return

            for i in range(target):

                if current_seq[0] in graph[i]:

                    helper([i]+current_seq)

        helper([target])

        return ans


# @lc code=end
