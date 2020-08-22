# transform one string into the "compressed" version of itself by converting all repeated letters into the form "[letter][count]"

def string_compression(s):
    # brute force: go through and count all continuous substrings and create a new string with those letters/counts
    # time: O(n-1)

    if len(s) == 1:
        return s

    j = 1
    curr_count = 1
    new_str = ""
    for i in range(len(s)):
        # check if we're at the end of the string
        if j != len(s):
            if s[i] == s[j]:
                curr_count += 1
            else:
                new_str += s[i] + str(curr_count)
                curr_count = 1
        else: # we've reached the end of the string (i == len(s)-1)
            if s[i] != s[i-1]:
                curr_count = 1
            new_str += s[i] + str(curr_count)
        
        j += 1
    
    return new_str if len(s) > len(new_str) else s