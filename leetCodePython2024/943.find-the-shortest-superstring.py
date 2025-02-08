#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#

# @lc code=start

class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        # given any strings in the words is not a substring of the others

        length = len(A)

        # additional len on top of first word,
        # if two words contatnation that has the same chars at the ending of a and the beginging of b
        # a = alex,b = leetcode
        # temp[a][b] = 8
        temp = [[0 for _ in range(length)] for _ in range(length)]

        # binary number 010 represents the second word is used but the first one and the third one
        # dp[i][j] i -> binary representation of used word seq, j-> ends with j-th word, dp-> the min length of the cancatenated string of (i,j)
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
                    # 1<<j bigger than s -> I think this def is wrong

                    # updated definition -> s: seq of filled digit
                    # this condition implies j is not included in s
                    continue

                # for every digits in s except j's are all filled up
                # if s = 100, j =4 then ps = 000 not 011
                # ~x returns the complement of x
                ps = s & ~(1 << j)
                # print('----------')
                # print('{0: b}'.format(s))
                # print('{0: b}'.format(ps))
                # print('----------')

                # all possible combination of b.r. that start with ps and end with j
                for i in range(length):
                    # s except j's are all filled up + end by j for all possible ending string form previous steps
                    # adding j to the last digit
                    if dp[ps][i] + temp[i][j] < dp[s][j]:
                        dp[s][j] = dp[ps][i] + temp[i][j]
                        parent[s][j] = i
        # print(parent[-1])

        placeholder = float('inf')
        ending = -1

        mask = (1 << length) - 1

        for i in range(length):

            if dp[mask][i] < placeholder:
                placeholder = dp[mask][i]
                ending = i

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
        # print(temp)
        # print(dp[-1])
        # print(parent[-1])

        return current
# @lc code=end
