#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque


class Solution:

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
            # print(queue)
            step += 1
            # if step > self.default_len+1:
            #     break

            for k in range(len(queue)):
                current = queue.popleft()
            # print(current)
                if current == end:
                    return step 

            # if 1 == 1:

                # if current not in self.pos_cache:
                #     self.pos_cache[current] = []

                for i in range(len(current)):
                    for ch in ['A','C','G','T']:
                        if ch != current[i]:
                            temp = current[:i] + ch + current[i + 1:]
                            # temp = [*current]
                            # temp[i]=ch
                            # temp = ''.join(temp)
                            if temp in bank:
                                bank.remove(temp)

                                if temp not in local_set:
                                    # if temp in bank:
                                    if temp == end:
                                        return step
                                    else:

                                        queue.append(temp)
                                        local_set.add(temp)



        return -1
# @lc code=end
