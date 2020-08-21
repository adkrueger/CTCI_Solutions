# given a string, check if it's a permutation of a palindrome
def palindrome_permutation(s):
    # brute force: check to see each of the permutations of the string and if they form a palindrome:
    # this would take O(n!n) (I think? n! for the permutations, n because you check each 
    # perm once over to see if it's palindromic)

    # my solution: put all characters into a hash, and keep track of if there are any characters that appear
    # an odd number of times. then, check if any other characters appear an odd number of times: if so, it
    # can't be a palindrome. oh, and ignore spaces (because that's what the book seems to do)
    # this would be O(nk) time, where n is the length of the string and k is the number of unique characters in s 
    d = {}
    s = s.lower()
    for c in s:
        if c != ' ':
            try:
                d[c] += 1
            except:
                d[c] = 1
    
    check = False
    for k in d:
        if d[k]%2:
            if check:
                return False
            check = True

    return True

