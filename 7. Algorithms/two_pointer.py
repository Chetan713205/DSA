def maxArea(l: list[int]) -> int:
    left=0
    right=len(l)-1
    max_area=0
    while left<right:
        width=right-left
        length=min(l[right], l[left])
        current_area=width*length
        max_area=max(max_area, current_area)
        if l[left]<l[right]:
            left+=1
        else:
            right-=1
    return max_area
    
l=[1,8,6,2,5,4,8,3,7]
print(maxArea(l))

'''
height = [1,8,6,2,5,4,8,3,7]

Index:   0  1  2  3  4  5  6  7  8
Value:   1  8  6  2  5  4  8  3  7

The lines: |  |  |  |  |  |  |  |  |
           1  8  6  2  5  4  8  3  7

Best container: between index 1 (height 8) and index 8 (height 7)
Width = 7 (distance between indices)
Height = min(8, 7) = 7
Area = 7 × 7 = 49

'''