import sys
input = sys.stdin.readline

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]

            if p == p[::-1]:
                print(p)
                exit(0)

    print(0)