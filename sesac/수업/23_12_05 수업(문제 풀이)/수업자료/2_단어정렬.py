import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

N = int(input())

words = [input().rstrip() for _ in range(N)]

words = list(set(words))    # 중복 제거

words.sort()
words.sort(key = lambda x : len(x))
# 또는 words.sort(key = lambda x : (len(x), x))

for word in words:
    print(word)