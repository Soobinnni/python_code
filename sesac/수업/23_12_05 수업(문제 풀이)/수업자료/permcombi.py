from itertools import permutations, combinations

nums = [1, 2, 3]
perm = permutations(nums, 2)
combi = combinations(nums, 2)

print(perm)
print(combi)
# print(list(perm))
# print(list(combi))

# words = ['aaba', 'ba', 'ababa', 'bbaa', 'baaba']

# for word1, word2 in permutations(words, 2):
#     p = word1 + word2

#     print(p)