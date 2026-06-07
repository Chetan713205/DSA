s="ABABBA"
k=2
left=0
count={}
result=0

for right in range(len(s)):
    if s[right] not in count:
        count[s[right]]=1
    else:
        count[s[right]]+=1

    while (right-left+1) - max(count.values())> k: 
        count[s[left]]-=1
        left+=1
    result=max(result, right-left+1)

print(result )

'''

consider "ABABBA" --> (5-0+1) - 3 > 2 = 3 > 2 == SATISFIES so result doesnot gets counted
consider "ABABB"  --> (4-0+1) - 3 > 2 = 2 > 2 == NOT SATISFIES so result gets counted

'''