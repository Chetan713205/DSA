"""
It allows fast retrieval of values based on keys by a process known as Hashing.
Each key is transformed into unique index through a hashing function, which can be used to access 
value in constant time. 
"""

nums=[1,2,2,3,3,1,1,4,2]
d={}
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


words=['eat', 'tea', 'tan', 'ate', 'nat', 'bat']     ##Anagrams
d={}
for i in words:
    sorted_word=''.join(sorted(i))
    if sorted_word in d:
        d[sorted_word].append(i)
    else:
        d[sorted_word]=[i]

print(list(d.items()))
print(d.values())
## [('aet', ['eat', 'tea', 'ate']), ('ant', ['tan', 'nat']), ('abt', ['bat'])]


n = [1, 2, 3, 4]
## check for duplicates
def check_for_duplicates(n):
    d={}
    for i in n:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    
    for values in d.values():
        if values>1:
            return "False"
            break

    return "True"
print(check_for_duplicates(n))


s="swiss"
def first_non_repete(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    for key, value in d.items():
        if value ==1:
            return key
print(first_non_repete(s))