#
# @lc app=leetcode id=582 lang=python3
#
# [582] Kill Process
#

# @lc code=start
from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)

        for i in range(len(ppid)):
            graph[ppid[i]].append(pid[i])
        
        ans = set()
        def helper(node):
            for i in graph[node]:
                ans.add(i)
                helper(i)

        ans.add(kill)
        helper(kill)

        return ans        
# @lc code=end

