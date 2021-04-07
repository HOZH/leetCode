#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque


class Solution:
    # bfs for finding shorest path in unweighted graph
    def minMutation(self, start: str, end: str, bank) -> int:
        self.default_len = len(bank)
        bank = set(bank)
        self.pos_cache = dict()

        if end not in bank:
            return -1

        queue = deque([start])

        step = 0
        while len(queue) > 0:
            local_set = set()
            step += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == end:
                    return step

                for i in range(len(current)):
                    for ch in ['A', 'C', 'G', 'T']:
                        if ch != current[i]:
                            temp = current[:i] + ch + current[i + 1:]

                            if temp in bank:
                                bank.remove(temp)

                                if temp not in local_set:
                                    if temp == end:
                                        return step
                                    else:

                                        queue.append(temp)
                                        local_set.add(temp)

        return -1
# @lc code=end
