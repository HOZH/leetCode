#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#

# @lc code=start


class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        length = len(A)

        # same chars at the ending of a and the beginging of b
        temp = [[0 for _ in range(length)] for _ in range(length)]

        #
        dp = [[241 for _ in range(length)] for _ in range(1 << length)]
        parent = [[-1 for _ in range(length)] for _ in range(1 << length)]

        # init dp values with first visited node
        for i in range(length):
            dp[1 << i][i] = len(A[i])

        for i in range(length):
            for j in range(length):
                temp_i, temp_j = A[i], A[j]
                temp_len = len(A[j])

                if i == j:
                    temp[i][j] = 0
                else:
                    count = 0

                    # for k in range(1, len(A[i]) + 1):
                    for k in range(len(A[i]), 0, -1):

                        if k < temp_len + 1:

                            a = temp_i[-k:]
                            b = temp_j[:k]

                            if a == b:
                                count = k
                                break

                        # else:
                        #     break

                    temp[i][j] = temp_len - count
        # s -> binary representation of indexs of eles that already visited

        # all possible binary representations
        for s in range(1, (1 << length)):
            # all possible b.r. end contains j's number
            for j in range(length):

                if not (s & (1 << j)):
                    # 1<<j bigger than s
                    continue

                # s except j's are all filled up
                ps = s & ~(1 << j)

                # all possible combination of b.r. that start with ps and end with j
                for i in range(length):
                    # s except j's are all filled up + end by j for all possible ending string form previous steps
                    if dp[ps][i] + temp[i][j] < dp[s][j]:
                        dp[s][j] = dp[ps][i] + temp[i][j]
                        parent[s][j] = i

        placeholder = float('inf')
        ending = -1
        for i in range(length):

            if dp[(1 << length) - 1][i] < placeholder:
                placeholder = dp[(1 << length) - 1][i]
                ending = i

        mask = (1 << length) - 1
        current = ''
        while mask != 0:

            placeholder = parent[mask][ending]

            mask = mask & ~(1 << ending)
            if mask != 0:

                current = A[ending][-temp[placeholder][ending]:] + current

            else:
                current = A[ending] + current
                break

            ending = placeholder

        return current


# @lc code=end
