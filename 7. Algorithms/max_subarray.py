nums=[   -2,    1,    -3,    4,    -1,    2,    1,    -5,    4   ]

##              1,1   -2,1   4,4   3,4    5,5   6,6   1,6    5,6

def find(nums: list) -> int:
    current_sum=nums[0]
    max_sum=nums[0]
    for i in nums[1:]:
        current_sum=max(i, current_sum+i)
        max_sum=max(max_sum, current_sum)
    return max_sum

print(find(nums))