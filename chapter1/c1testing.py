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

# test part 6

# test part 7

# test part 8

# test part 9
