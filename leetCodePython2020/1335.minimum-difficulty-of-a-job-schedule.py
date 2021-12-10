#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        task_count = len(jobDifficulty)
        if task_count < d:
            return -1

        # dp[i][j] min score finshed j tasks in i days
        dp = [[float('inf') for _ in range(task_count + 1)]
              for _ in range(d + 1)]
        dp[0] = [0 for _ in range(task_count + 1)]

        for current_day in range(1, d + 1):
            max_tasks_til_today = task_count + 1-(d-current_day)
            min_prev_finished = current_day - 1
            for today_finished in range(current_day, max_tasks_til_today):
                for prev_finished in range(min_prev_finished, today_finished):
                    if current_day == 1 and prev_finished >= 1:
                        continue
                    dp[current_day][today_finished] = min(
                        dp[current_day][today_finished], dp[current_day - 1][prev_finished] + max(
                            jobDifficulty[prev_finished:today_finished]))

        return dp[-1][-1]

# @lc code=end
