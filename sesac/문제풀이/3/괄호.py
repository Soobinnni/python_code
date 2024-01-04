# https://www.acmicpc.net/problem/9012

from collections import deque

def first():
    N = int(input())
    brackets = [list(map(str, input())) for _ in range(N)]
    ans = 'NO'

    for bracket in brackets:
        Q = deque()
        for b in bracket:
            if b == '(': Q.append(b)

            if b == ')':
                if Q:
                    Q.popleft()
                else:
                    ans = 'NO'
                    break
        else:
            if Q:
                ans = 'NO'
            else:
                ans = 'YES'
        print(ans)


def second():
    N = int(input())
    brackets = [list(map(str, input())) for _ in range(N)]

    for bracket in brackets:
        Q = []
        for b in bracket:
            if b == '(': Q.append(b)

            if b == ')':
                if Q: Q.pop()
                else:
                    Q = True
                    break

        print('NO' if Q else 'YES')

def third():
    for _ in range(int(input())):
        bracket = list(map(str, input()))
        stack = []
        for b in bracket:
            if b == '(': stack.append(b)

            if b == ')':
                if stack:
                    stack.pop()
                else:
                    stack = True
                    break

        print('NO' if stack else 'YES')

third()