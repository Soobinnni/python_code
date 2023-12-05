def solution1():
    num = int(input())
    words = set(input() for i in range(num))
    len_word_dict = dict(zip(words, map(len, words)))
    ans = sorted(len_word_dict.items(), key=lambda x: (x[1], x[0]))

    for a, _ in ans:
        print(a)

def solution2():
    N = int(input())
    words = [input().rstip() for _ in range(N)]

    words = list(set(words))
    words.sort() # 알파벳 순으로 정렬
    words.sort(key = lambda x: len(x)) # 길이 기준으로 정렬할 것임을 알림

    for word in words:
        print(word)
