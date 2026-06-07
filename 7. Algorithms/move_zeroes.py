nums = [0, 1, 0, 3, 12]

def move_zeroes(nums: list) -> list:
    non_zero_pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[non_zero_pos]=nums[i]
            non_zero_pos+=1 
    
    for i in range(non_zero_pos, len(nums)):
        nums[i]=0
    return nums

print(move_zeroes(nums))