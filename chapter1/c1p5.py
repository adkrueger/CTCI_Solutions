# given two strings, find if one of the following operations has been performed on the first to reach the second:
# add a letter, remove a letter, or replace a letter

def one_away(s1, s2):
    # brute force: check to see if any of the letters are removed, then if any of the letters are added, then if any letters are replaced

    # my solution: go through each string with one number iterator
    # use this to check if either of the letters match: if they do, then move on
    # if they don't, then need to flag the missing/replaced letter
    if s1==s2:
        return True
    elif abs(len(s1)-len(s2))>=2:
        return False
    
    # treat the smaller string as the one we're checking (makes addition case easier)
    if len(s1)!=len(s2):
        return check_smaller(s1, s2) if len(s1)<len(s2) else check_smaller(s2, s1)
    else:
        flag = 0
        j = 0

        for i in range(len(s1)):
            if s1[i] != s2[j]:
                flag += 1

            if flag>1:
                return False
            
            j = i + flag
        
        return True

def check_smaller(s1, s2):
    flag = 0
    j = 0

    for i in range(len(s1)):
        j = i
        if s1[i] != s2[j]:
            flag += 1
            s1 = s1[0:i] + s2[j] + s1[i:len(s1)]

        if flag>1:
            return False
        
    
    return True