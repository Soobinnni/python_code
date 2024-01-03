# https://www.acmicpc.net/problem/2164

# N장의 카드, 제일 위부터 아래는 오름차순으로 쌓임
# 다음과 같은 동작을 카드가 한 장 남을 때까지 반복 
    # 1. 제일 위에 있는 카드를 바닥에 버린다. 
    # 2. 다음으로 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# 예시: 1234 -> (1버림, 2아래에) 342 -> (3버림, 4 아래에) 24 -> (2버림, 아래에 둘 카드 없음) 4
       # ans == 4

from collections import deque

cards = deque([i+1 for i in range(int(input()))])
while len(cards) > 1:
    cards.popleft()
    behind_card = cards.popleft()
    cards.append(behind_card)

print(cards[0])