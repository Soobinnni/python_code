def solution():
    # 반례 : c의 인덱스는 그대로지만, c는 b를 추월함
    # 4, [a,b,c,d], [d,a,c,b]
    # 정답2
    # 출력1
    k = int(input())
    d, y = [[input() for _ in range(k)] for _ in range(2)]
    cnt = 0
    for car in y:
        if y.index(car) < d.index(car): cnt += 1

    print(cnt)


def solution2(): # 내 최종 답변
    k = int(input())
    d = {input(): i for i in range(k)}
    y = [d[input()] for _ in range(k)]
    cnt = 0
    for i in range(1, k):
        if y[i-1] > min(y[i:]): cnt+=1
    print(cnt)

def solution3(): # 딕셔너리 활용
    N = int(input())

    in_order = dict()
    for order in range(N):
        in_order[input()] = order  # 차량번호 : 들어간 순서로 맵핑

    out_order = []
    for _ in range(N):
        out_order.append(in_order[input()])  # 나온 순서대로 들어간 순서 기록

    standard = N
    cnt = 0

    for i in range(N - 1, -1, -1):  # 가장 나중에 나온 차부터 보면서
        if out_order[i] > standard:  # 내 뒤에 나보다 먼저 들어간 차가 있다면
            cnt += 1  # 추월 기록

        else:  # 아니라면
            standard = out_order[i]  # 기준 갱신

    print(cnt)

def solution4(): # 리스트 인덱스 활용
    N = int(input())

    in_order = []
    for _ in range(N):
        in_order.append(input())  # 입장 순서대로 리스트에 추가

    out_order = []
    for _ in range(N):
        out_order.append(in_order.index(input()))  # 나간 순서대로 입장 시 순위(인덱스)를 새로운 리스트에 추가

    standard = N  # 기준은 뒤에 있는 차 중에 입장 순서가 가장 빠른 차
    cnt = 0
    for i in range(N - 1, -1, -1):  # 거꾸로 돌면서
        if out_order[i] > standard:  # 나간 순서가 기준보다 크다면(내 뒤에 나보다 먼저 들어간 차가 있다면)
            cnt += 1  # 반드시 추월을 한 것임

        else:  # 아니라면
            standard = out_order[i]  # 기준 갱신

    print(cnt)