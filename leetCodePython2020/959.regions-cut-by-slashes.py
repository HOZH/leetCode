#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#

# @lc code=start


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        ops = [[] for _ in range(n)]

        parents = [k for k in range(n ** 2 * 4)]
        # rank = [1 for k in range(n ** 2 * 4)]

        for i in range(n):
            for j in grid[i]:
                ops[i].append(j)

        row_index, col_index = 0, 0

        def find(current):

            if parents[current] != current:
                parents[current] = find(parents[current])

            return parents[current]

        def merge(a, b):
            # can be optimize by lowering the layers of tree structure
            # temp_a, temp_b = find(a), find(b)
            # if rank[a] > rank[b]:
            #     parents[temp_b] = parents[temp_a]

            # elif rank[a] < rank[b]:
            #     parents[temp_a] = parents[temp_b]

            # else:
            #     parents[temp_a] = parents[temp_b]
            #     rank[b] += 1

            parents[find(a)] = find(b)

        for i in range(n):
            for j in range(n):

                # base index of current block
                base = i * (n * 4) + j * 4

                if ops[i][j] == '\\':
                    merge(base + 0, base + 1)
                    merge(base + 2, base + 3)

                elif ops[i][j] == '/':
                    merge(base + 0, base + 3)
                    merge(base + 1, base + 2)

                else:
                    merge(base + 0, base + 1)
                    merge(base + 1, base + 2)
                    merge(base + 2, base + 3)

                if i + 1 < n:
                    merge(base + 2, base + 4 * n + 0)
                if j + 1 < n:
                    merge(base + 1, base + 4 + 3)

        count = 0

        for i in range(n*n*4):
            if i == find(i):
                count += 1

        return count

        # @lc code=end
