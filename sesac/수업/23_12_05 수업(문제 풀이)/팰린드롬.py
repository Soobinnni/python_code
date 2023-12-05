# ==============================투포인터 알고리즘==============================
    # a = abaa
    # a[0] == a[3] ->회문일 가능성이 있음
    # a[1] != a[2] -> 회문이 아님!
    # l,s(left, start) / r, e(right, end)
    # l은 0부터 r은 -1부터 시작하며  l<r이고 |l| == |r|이면 마지막
def 투포인터_solution(w):
    l = 0
    r = len(w) - 1  # -1

    while l <r:
        if w[l] != w[r]:
            return False
        l += 1
        r -= 1

    return w

def print_투포인터():
    print(투포인터_solution(input().rstrip()))

    
# ==============================순열 문제(순서가 상관 있는 문제)==============================
# permutations 모듈 사용하기 permutations(순열) / combinations(조합)
from itertools import permutations, combinations

def ex():
    nums = [1,2,3]
    perm = permutations(nums, 2)
    combi = combinations(nums, 2)

    print(perm)
    print(combi)

    print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    print(list(combi)) # [(1, 2), (1, 3), (2, 3)]

def 순열_solution():
    words = [input() for _ in range(int(input()))]

    for word1, word2 in permutations(words, 2):
        p  = word1 + word2

        if p == p[::-1]:
            print(p)
            exit(0)

    print(0)
    
# break의 문제점 : 가장 가까운for문만 종료하고 나감
#               해결점 1) flag 사용한다, 하나씩 break 걸기(if 조건문을 계속 검사해야하는 문제점이 발생)
#               해결점 2) exit(0) : py 파일을 강제로 종료시키는 명령어(이후 로직이 존재한다면, 파일이 종료되는 것이 난감한 문제점이 발생)
#               해결점 3) for문을 하나의 함수로 만들고 return 처리(함수 종료) 즉, for문이 다중으로 있는 경우 함수화하여 return처리로 함수를 종료시켜 버림