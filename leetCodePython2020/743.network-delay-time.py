#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # need to be a dag

        delay = [1e8] * (N + 1)
        delay[K] = 0
        delay[0] = -1

        dag = defaultdict(list)

        for i, j, c in times:
            dag[i].append([j, c])

        queue = deque()
        queue.append(K)

        visited = set()

        while len(queue) > 0:
            current = queue.popleft()
            for i, c in dag[current]:
                if delay[current] + c < delay[i]:
                    delay[i] = delay[current] + c

            l = sorted(dag[current], key=lambda x: x[1])

            visited.add(current)

            min_cost = 1e9
            mid = None

            for i in range(1, len(delay)):
                # print(min_cost,delay[i])
                # print(delay)

                if i not in visited:
                    if delay[i] < min_cost:
                        mid = i
                        min_cost = delay[i]

            # print(mid)
            if mid is not None:
                queue.append(mid)

        # print(delay)
        temp = max(delay[1:])

        if temp >= 1e8:
            return -1

        else:
            return temp

# @lc code=end
