#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start
from collections import defaultdict, Counter


class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        """
        Time and Space Complexities:
        O(nlogn + n*k^3), O(n+p)
        # n - no.of users
        # p - no of patterns
        # k - average no of websites per user - max can be n
        """

        # Step 1: Sort the input by timestamp - O(nlogn)
        data = sorted(zip(timestamp, username, website))

        # Step 2: Group websites visited by each user in order of time - O(n)
        userVisits = defaultdict(list)
        for _, user, site in data:
            userVisits[user].append(site)

        # Step 3: Count 3-sequence patterns across all users - O(n*k^3)
        patternCount = Counter()
        for user, sites in userVisits.items():
            n = len(sites)
            seenPatterns = set()  # Avoid counting duplicate patterns for the same user
            # unique_patterns = set(combinations(sites, 3))
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        if pattern not in seenPatterns:
                            seenPatterns.add(pattern)
                            patternCount[pattern] += 1

        # Step 4: Find the pattern with the highest count
        # Break ties lexicographically (default behavior of tuples in Python)
        # max picks the first element - if same count is fount, first is the lexografically small in soreted
        maxPattern = max(sorted(patternCount), key=lambda p: patternCount[p])

        return list(maxPattern)
# @lc code=end

