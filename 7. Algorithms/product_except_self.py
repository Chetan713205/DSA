nums=     [1,       2,          3,     4]
#output=  [1,       1,          2,     6]
#        24,24     12,24       8,12    6,4
#        24          12          8       6


def product_except_self(nums):
    n=len(nums)
    output=[1]*n
    print(output)
    
    prefix=1
    for i in range(n):
        output[i]=prefix
        prefix*=nums[i]
        
    print(output)
    
    suffix=1
    for i in range(n-1, -1, -1):
        output[i]*=suffix
        suffix*=nums[i]
    print(output)

product_except_self(nums)