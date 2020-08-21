# given two strings, find out if one is a permutation of the other
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    elif s1 == s2:
        return True


    # brute force
    # make s1 into all possible configurations of itself, then check if 
    # any of those spell out s2. 
    # this would be O(n!m)

    # otherwise, put all of s1 into its own hashmap by letter,
    # adding 1 for each appearance of a letter. then subtract 1 for each 
    # appearance of that letter in s2
    # this should be O(nm) time
    d1 = {}
    for c in s1:
        try:
            d1[c] += 1
        except:
            d1[c] = 1
    
    for c in s2:
        try:
            d1[c] -= 1
            if d1[c] < 0:
                return False
        except:
            return False
    
    return True