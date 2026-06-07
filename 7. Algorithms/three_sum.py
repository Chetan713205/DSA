nums = [-1,0,1,2,-1,-4]

def three_sum(nums: list)-> list:
    n=len(nums)
    nums.sort()
    answer=[]
    
    for i in range(n):
        if nums[i]>0:
            break
        elif i>0 and nums[i]==nums[i-1]:
            continue
        
        lo=i+1
        hi=n-1
        while lo<hi:
            summ=nums[i]+nums[lo]+nums[hi]
            if summ==0:
                answer.append([nums[i], nums[lo], nums[hi]])
                lo=lo+1
                hi=hi-1
                while lo<hi and nums[lo]==nums[lo-1]:       # skip duplicates
                    lo+=1
                while lo<hi and nums[hi]==nums[hi+1]:       # skip duplicates
                    hi-=1
            
            elif summ<0:
                lo+=1
            else:
                hi-=1
    return answer
    
print(three_sum(nums))

## o/p: [[-1, -1, 2], [-1, 0, 1]]