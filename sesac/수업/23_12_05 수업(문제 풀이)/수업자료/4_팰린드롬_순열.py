import sys
input = sys.stdin.readline
from itertools import permutations

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for word1, word2 in permutations(words, 2):
        p = word1 + word2

        if p == p[::-1]:
            print(p)
            exit(0)
    
    print(0)