#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        bag = {}
        for i in range(len(sorted_scores)):
            value = sorted_scores[i]
            bag[value] = str(i+1)

        medal_mapping = {'1': "Gold Medal",
                         '2': "Silver Medal", '3': "Bronze Medal"}

        return list(map(lambda x: bag[x] if bag[x] not in {'1', '2', '3'} else medal_mapping[bag[x]], score))
        # sorted_scores = sorted(score, reverse=True)
        # bag = {}
        # for index, value in enumerate(sorted_scores):
        #     if index == 0:
        #         bag[value] = "Gold Medal"
        #     elif index == 1:
        #         bag[value] = "Silver Medal"
        #     elif index == 2:
        #         bag[value] = "Bronze Medal"
        #     else:
        #         bag[value] = str(index + 1)

        # return list(map(lambda x: bag[x], score))


# @lc code=end
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        if len(score) == 1:
            return medals[:1]

            #  score = [10,3,8,9,4]
        mapping = {}
        for i, s in enumerate(score):
            # {10: 0, 3: 1, 8: 2, ...}
            mapping[s] = i

        # [10,9,8,4,3]
        sorted_scores = sorted(score, reverse=True)


        output = [0 for x in range(len(score))]  # [0, 0, 0, 0, 0]
        # {10: 0, 3: 1, 8: 2, ...}

        for i, ss in enumerate(sorted_scores):  # [10,9,8,4,3]
            value = sorted_scores[i]  # 10
            original_index = mapping[ss]  # 0
            if i+1 <= 3:
                output[original_index] = medals[i]  # or +1 -1
            else:
                output[original_index] = str(i+1)  # output = ["1", 0, 0, 0, 0]
        return output
["Gold Medal","Silver Medal","3","4","5"]