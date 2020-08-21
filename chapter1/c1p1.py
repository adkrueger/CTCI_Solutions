# determine if a string has all unique characters
def allUnique(s):
    # brute force
    '''
    for c in range(len(s)):
        for i in range(c+1, len(s)):
            if s[c] == s[i]:
                return False
    '''

    # O(n) time using hash map
    d = {}
    for c in s:
        try:
            return d[c]
        except:
            d[c] = False

    return True
