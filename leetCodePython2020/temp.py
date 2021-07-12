






from itertools import permutations
test = [10,4,-8,7]


def foo(arr):


    left_sum,right_sum = sum(arr),0

    count = 0

    for i in range(len(arr)-1,0,-1):

        temp = arr[i]

        left_sum-=temp
        right_sum+=temp

        count += 0 if left_sum <= right_sum else 1

    return count

print(foo(test))        


a = "GeEK"

# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(a)

# Print the obtained permutations
for j in set(p):
    print(j)
