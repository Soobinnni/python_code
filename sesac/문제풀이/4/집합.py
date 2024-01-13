# https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline
S = set()

for _ in range(int(input())):
    request = input().rstrip()

    if ' ' in request:
        request_num = request.split()
        re, num = request_num[0], int(request_num[1])

        if re == 'add':
            S.add(num)
        if re == 'remove':
            S = S - {num}
        if re == 'check':
            print(1 if num in S else 0)
        if re == 'toggle':
            S.remove(num) if num in S else S.add(num)
    if request == 'all':
        S = set(range(1, 21))
    if request == 'empty':
        S.clear()