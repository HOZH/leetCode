#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0

        left = 0
        char_count = defaultdict(int)  # 统计字符出现次数
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1  # 收缩窗口

            max_length = max(max_length, right - left + 1)

        return max_length
        
# @lc code=end

