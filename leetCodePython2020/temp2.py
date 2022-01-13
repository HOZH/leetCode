class Solution:
    def checkRecord(self, s: str) -> bool:

        consecutive_lates, absents = 0, 0

        for i in s:
            if i == 'L':
                consecutive_lates += 1
                if consecutive_lates > 2:
                    return False
            else:
                if i == 'A':
                    absents += 1
                if absents > 1:
                    return False
        return True


class Solution:
    def checkRecord(self, s: str) -> bool:
        late_count = 0
        absent_count = 0
        for i in range(len(s)):

            if s[i] != 'L':
                late_count = 0
            else:
                late_count += 1
            if s[i] == 'A':
                absent_count += 1
            if late_count >= 3 or absent_count >= 2:
                return False
        return True
