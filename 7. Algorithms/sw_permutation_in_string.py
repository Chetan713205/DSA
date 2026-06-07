s1="eidbaooo"
s2="ab"

def checkInclusion_v2(s1, s2):
    if len(s2)>len(s1):
        return False 
    window=[]
    window_length=len(s2)
    for right in range(len(s1)):
        window.append(s1[right])

        if len(window)>window_length:
            window.pop(0)
        
        if sorted(window)==sorted(s2):
            return True
    
    return False

print(checkInclusion_v2(s1, s2))