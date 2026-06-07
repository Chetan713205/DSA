from collections import Counter

def findAnagrams(s: str, p: str):
    res = []
    p_count = Counter(p)            # Converts into dictionary
    window = Counter()              # Converts into dictionary

    k = len(p)

    for i in range(len(s)):
        window[s[i]] += 1

    if i >= k:
        # Remove the character that is going out of the sliding window
        # (i-k is the index of the leftmost character of previous window)
        # Checks if the last element has frequency 1
        if window[s[i-k]] == 1:
            # If its count becomes 0, remove it from dictionary to keep it clean
            del window[s[i-k]]
        else:
            # Otherwise, just decrease its frequency
            window[s[i-k]] -= 1


    # If current window matches p's frequency,
    # store starting index of the anagram
    res.append(i - k + 1)   # start index = current index - window size + 1

    return res