#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        self.ans = []
        n = len(graph) - 1

        def dfs(node_index, current_path):
            current_path = current_path+[node_index]
            if node_index == n:
                self.ans.append(current_path)
                return
            next_node_indexs = graph[node_index]
            for i in next_node_indexs:
                dfs(i, current_path)

        dfs(0, [])
        return self.ans


# @lc code=end
