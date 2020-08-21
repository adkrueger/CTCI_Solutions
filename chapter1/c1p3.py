# replace all spaces in a string with '%20'

def URLify(s, s_len):
    # go through each character and replace the space with '%20' (approximately O(n) time)
    url = ''
    for i in range(s_len):
        if s[i] == ' ':
            url += '%20'
        else:
            url += s[i]
            

    return url