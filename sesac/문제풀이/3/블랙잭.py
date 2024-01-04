# https://www.acmicpc.net/problem/2798

# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임

# 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

# 플레이어는 양의 정수인 카드들을 가지고 있다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

# 3장의 카드를 뽑아 3장의 합이 M과 가깝도록 하여 그 수를 출력
from itertools import combinations

def first():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    ans = 0
    before_subtracted_value = 99999

    for a, b, c in combinations(cards, 3):
        num = sum([a, b, c])
        subtracted = M - num

        if (subtracted >= 0) and (subtracted < before_subtracted_value):
            before_subtracted_value = subtracted
            ans = num

    print(ans)

def second():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    ans = 0
    before_subtracted_value = 99999

    for nums in combinations(cards, 3):
        num = sum(nums)
        subtracted = M - num

        if 0 <= subtracted < before_subtracted_value:
            before_subtracted_value = subtracted
            ans = num

    print(ans)

def third():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    max_point = 0

    for nums in combinations(cards, 3):
        num = sum(nums)

        if max_point < num <= M:
            max_point = num

    print(max_point)