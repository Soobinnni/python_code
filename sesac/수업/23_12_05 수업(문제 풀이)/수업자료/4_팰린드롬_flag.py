import sys
input = sys.stdin.readline

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    flag = False
    ans = 0

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            word = words[i] + words[j]

            if word == word[::-1]:
                ans = word
                flag = True
                break

        if flag == True:
            break

    print(ans)