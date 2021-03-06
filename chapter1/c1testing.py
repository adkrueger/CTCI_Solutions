import c1p1, c1p2, c1p3, c1p4, c1p5, c1p6, c1p7, c1p8, c1p9

# test part 1
assert not c1p1.allUnique('Hello World')
assert c1p1.allUnique('whats up')
assert not c1p1.allUnique('aaaaaaaaaaaaaaaaaaaaaa')
assert c1p1.allUnique('abcdefghijklmnopqrstuvwxyz')
print("Part 1 testing passed.")

# test part 2
assert c1p2.checkPermutation('abc', 'bac')
assert c1p2.checkPermutation('abc', 'abc')
assert not c1p2.checkPermutation('abc', 'abcc')
assert not c1p2.checkPermutation('abc', 'bbc')
assert not c1p2.checkPermutation('kslqpwofhoeljasflkjppbn', 'bbcjalshdkjahsdkjaskjdh')
print("Part 2 testing passed.")

# test part 3
assert c1p3.URLify('Mr John Smith     ', 13) == 'Mr%20John%20Smith'
assert c1p3.URLify('tyler , the creator     ', 19) ==  'tyler%20,%20the%20creator'
assert c1p3.URLify('hello world  ', 11) == 'hello%20world'
print("Part 3 testing passed.")

# test part 4
assert c1p4.palindrome_permutation('Tact Coa')
assert c1p4.palindrome_permutation('a man a plan a canal panama')
assert not c1p4.palindrome_permutation('this aint a palindrome feller')
print("Part 4 testing passed.")

# test part 5
assert c1p5.one_away('pale', 'ple')
assert c1p5.one_away('pales', 'pale')
assert c1p5.one_away('pale', 'bale')
assert c1p5.one_away('pale', 'pple')
assert c1p5.one_away('pale', 'paale')
assert c1p5.one_away('pale', 'ppale')
assert c1p5.one_away('pale', 'pale')
assert not c1p5.one_away('pale', 'blle')
assert not c1p5.one_away('pale', 'balek')
assert not c1p5.one_away('pale', 'aaaaaa')
assert not c1p5.one_away('pale', 'bppale')
assert not c1p5.one_away('pale', 'aa')
assert not c1p5.one_away('papap', 'apapa')
print("Part 5 testing passed.")

# test part 6
assert c1p6.string_compression('aabcccccaaa') == 'a2b1c5a3'
assert c1p6.string_compression('aabcccccaaaz') == 'a2b1c5a3z1'
assert c1p6.string_compression('abcccccaaa') == 'a1b1c5a3'
assert not c1p6.string_compression('aabcccccaaa') == 'a1b1c4a2'
assert not c1p6.string_compression('aabcccccaaa') == 'a2b1c5a2'
assert c1p6.string_compression('abca') == 'abca'
assert c1p6.string_compression('aabbccaa') == 'aabbccaa'
print("Part 6 testing passed.")


# test part 7
assert c1p7.rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print("Part 7 testing passed.")

# test part 8

# test part 9
