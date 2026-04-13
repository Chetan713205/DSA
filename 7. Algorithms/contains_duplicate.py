nums = [-1, -2, -3, -1]

def find(nums: list)-> bool:
    seen=set(nums)
    if len(seen)==len(nums):
        return False
    else:
        return True 
    
print(find(nums))