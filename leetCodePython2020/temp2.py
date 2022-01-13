class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        if not len(s):
            return False
        if s == goal and len(s)-len(set(s))<1:
            return False 

        diff_count = 0
        s_set, goal_set = set(), set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_count += 1
                s_set.add(s[i])
                goal_set.add(goal[i])
            if diff_count > 2:
                return False


        return s_set == goal_set
"""

        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False
        "ab"
"ab"
s"""

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        counter = Counter(s)
        if counter != Counter(goal): return False
        max_duplicate = max(counter.values())
        if max_duplicate<2 and s==goal:return False
        if max_duplicate>=2 and s==goal: return True
        count = 0
        for c1, c2 in zip(s, goal):
            if c1!=c2: count+=1
        return count == 2


class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        start = s.find('1')
        flag = True

        for i in range(start+1, len(s)):
            if s[i] == '1':
                if not flag:
                    return False

            elif s[i] == '0':
                flag = False

        return True
