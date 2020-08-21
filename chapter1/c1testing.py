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