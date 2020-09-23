
from collections import defaultdict


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    # Write your code here
    # first_half -> number of possible combination of prices of jeans and shoes
    # sec_half -> number of possible combination of prices of tops and skirts
    # dp -> dp[i] = sum(sec_half[:i+1]), for boosting up speed only
    # print(priceOfJeans)
    # print(priceOfShoes)
    # print(priceOfSkirts)
    # print(priceOfTops)
    # print(budgeted)
    # first_half,sec_half,dp = [0]*(budgeted+1),[0]*(budgeted+1),[0]*(budgeted+1)
    first_half, sec_half, dp = defaultdict(
        int), defaultdict(int), defaultdict(int)

    ans = 0

    for i in priceOfJeans:
        for j in priceOfShoes:
            if i+j < budgeted:
                first_half[i+j] += 1

    for i in priceOfSkirts:
        for j in priceOfTops:
            if i+j < budgeted:
                sec_half[i+j] += 1
    # print(first_half,sec_half)

    def foo(nums, target):
        length = len(nums)
        if length == 1:
            return 0 if target <= nums[0] else 1

        l, r = 0, length - 1
        while l <= r:
            pivot = l + (r - l) // 2

            if target == nums[pivot]:
                return pivot

            if target <= nums[pivot]:
                r = pivot - 1

            else:
                l = pivot + 1

            # else:
            #     return pivot
        return l
    # print(first_half)
    print(sec_half)

    # print(sec_half)
    sec_half_keys = list(sec_half.keys())
    sec_half_keys.sort()
    # print(sec_half_keys)
    for i in range(0,len(sec_half_keys)):
        dp[sec_half_keys[i]] = sec_half[sec_half_keys[i]]+(dp[sec_half_keys[i-1]] if i !=0 else 0)
    # print(dp)
    dp_keys = list(dp.keys())
    dp_keys.sort()
    # print(dp_keys)
    # print(foo(dp_keys,5.5))

    

    # for i in range(1,len(sec_half)):
    #     dp[i] = dp[i-1]+sec_half[i]

    for i in first_half.keys():
        first_part = first_half[i]
        if i < budgeted:
            sec_part_index = foo(dp_keys,budgeted-i)
            # if budgeted-i not in dp:
            #     sec_part_index-=1
            # print('sec',sec_part_index)
            # print(budgeted-i)
            # print(dp_keys)
            # print(dp)
            sec_part = dp[dp_keys[sec_part_index]]
            # sec_part=0
            # for j,val in sec_half.items():
            #     if j <= budgeted-i:
            #         sec_part += val
            # print(sec_part)
            
            ans += first_part*sec_part

    return ans


# print(getNumberOfOptions([2, 3], [4], [2, 3], [1, 2], 10))
print(getNumberOfOptions([4], [3,4,1], [3,2], [4], 12))
