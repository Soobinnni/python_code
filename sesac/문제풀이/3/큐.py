# https://www.acmicpc.net/problem/10845
from collections import deque
import sys
input = sys.stdin.readline

Q = deque()
for _ in range(int(input())):
    require = input().rstrip()
    if ' ' in require: Q.append(int(require.split()[1]))
    elif require == 'pop': print(Q.popleft() if Q else -1)
    elif require == 'size': print(len(Q))
    elif require == 'empty': print(0 if Q else 1)
    elif require == 'front': print(Q[0] if Q else -1)
    else: print(Q[-1] if Q else -1)