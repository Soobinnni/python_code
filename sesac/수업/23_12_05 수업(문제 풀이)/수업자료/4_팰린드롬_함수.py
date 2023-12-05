import sys
input = sys.stdin.readline

def find():
    global ans

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]

            if p == p[::-1]:
                ans = p
                return

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    ans = 0
    find()

    print(ans)