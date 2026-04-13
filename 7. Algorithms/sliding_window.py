def find(s: str) -> int:
    max_length=0
    left=0
    char_set=set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_length=max(max_length, right-left+1)
    return max_length


s="abcacbbb"
print(find(s))

'''

Initial: a b c b a
         ^   ^
         l   r (r=2, window="abc")

When r=3 (character 'b'):
Window: a b c b
        ^     ^
        l     r
        
Remove from left until 'b' is gone:
Step 1: a b c b  -> remove 'a'
          ^   ^
          l   r
Step 2: a b c b  -> remove 'b'
            ^ ^
            l r
            
Now add new 'b': c b
                 ^ ^
                 l r

'''