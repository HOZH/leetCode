



temp=[1,2,3,4,5]
l_pt,r_pt = 0,len(temp)-1
m=0
target = 2


while l_pt < r_pt:

            m = l_pt+(r_pt-l_pt)//2

            current = temp[m]

            if current==target:
                
                break
            elif current>target:
                r_pt=m-1
            else:
                l_pt=m+1

temp = [1, 2, 3, 4, 5]
l_pt, r_pt = 0, len(temp) - 1
m = 0
target = 4

while l_pt < r_pt:

    m = l_pt + (r_pt - l_pt) // 2

    current = temp[m]

    if current == target:
        l_pt=m

        break
    elif current > target:
        r_pt = m - 1
    else:
        l_pt = m + 1

print(l_pt)


print(m)

