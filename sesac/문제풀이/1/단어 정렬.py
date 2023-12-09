words = set(input() for _ in range(int(input())))
words_len_dict = dict(zip(words, map(len, words)))
ans = sorted(words_len_dict.items(), key = lambda x: (x[1], x[0]))
for k, _ in ans:
    print(k)