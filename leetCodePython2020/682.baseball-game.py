#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start


class Solution:
    def calPoints(self, ops: List[str]) -> int:

        ans = 0
        rounds = []

        for i in range(len(ops)):

            try:
                int(ops[i])
                flag = True
            except ValueError:
                flag = False

            if flag:

                ans += int(ops[i])
                rounds.append(int(ops[i]))

            elif ops[i] == '+':
                ans += sum(rounds[-2:])
                rounds.append(sum(rounds[-2:]))
                # print(rounds[:-2],rounds)
            elif ops[i] == 'D':
                if len(rounds):
                    ans += 2*rounds[-1]
                    rounds.append(2*rounds[-1])
            else:
                if len(rounds):
                    ans -= rounds[-1]

                    rounds = rounds[:-1]
            # print(ans)

        return ans


# @lc code=end
