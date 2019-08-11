#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #said order doesn't matter but still can't pass some of the  test cases with dict() approach
        dic = dict()
        for i in range(len(list1)):

            dic[list1[i]]=i

        answers = list()

        for i in range(len(list2)):

            if list2[i] in dic:

                answers.append((dic[list2[i]]+i, list2[i]))

        answers.sort()

        if len(answers) == 0:
            return []
        first_weight = answers[0][0]

        final = list()

        for i in answers:

            if i[0] == first_weight:
                final.append(i[1])
            else:
                break

        return final

        # temp_list = list((collections.Counter(list1) &
        #                   collections.Counter(list2)).elements())

        # if len(temp_list) == 0:
        #     return []

        # costs, answers = list(), list()

        # for i in temp_list:

        #     costs.append(list1.index(i)+list2.index(i))

        # answer_list = list(zip(temp_list, costs))

        # first_weight = answer_list[0][1]

        # for i, j in answer_list:

        #     if j == first_weight:

        #         answers.append(i)

        #     else:
        #         break

        # return answers
