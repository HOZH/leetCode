#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:


        a=list(filter(lambda x:x%60==0,time))
        b = list(filter(lambda x: x % 60 != 0, time))

        # print(a)
        a_len = len(a)
        time_len =len(time)

        count = a_len*(a_len-1)
        print(len(a))
        print(len(time))
        print(count)

        temp = itertools.combinations(b, 2)

        # # lis = list(temp)

        # mapped = (map(lambda x: x[0]+x[1], temp))

        # # return functools.reduce()

        # # return sum(map(lambda i: i % 60 ==0, mapped))

        # # return sum(1 for i in mapped if i%60==0)

        # count = 0

        for i in enumerate(temp):
            # print(i)
            if (i[1][0]+i[1][1]) % 60 == 0:

                count += 1

        # return count

        # return len(tuple(filter(lambda x:x %60==0,mapped)))

        # while True:

        #     pass

        # return sum(map(lambda i: i % 60 == 0, map(lambda x: x[0]+x[1], itertools.combinations(time, 2))))

        # print(type(temp))
