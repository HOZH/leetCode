#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        counts = defaultdict(int)

        while len(cpdomains):

            current_count, current_domain = cpdomains.pop().split(' ')
            counts[current_domain] += int(current_count)

            temp = current_domain.split('.')

            if len(temp) > 1:
                new_string = current_count+' '+'.'.join(temp[1:])
                cpdomains.append(new_string)

        result = []

        for i, j in counts.items():
            result.append(str(j)+' '+i)

        return result


# @lc code=end
