def solution(): # 내가 낸 최종 답변
    l = int(input())
    roads = list(map(int, input().split()))
    ans = [0]

    if l < 3:
        if l == 2 and roads[0] >= roads[1]: ans = roads[1]-roads[0]
    else:
        a = b = roads[l-1]

        for i in range(l-2, -1, -1):
            if b > roads[i]:
                ans.append(a - roads[i])
                b = roads[i]
            else:
                a = b = roads[i]

    print(max(ans))

def solution2():
    N = int(input())
    road = list(map(int, input().split()))

    now_height, max_height = 0, 0  # 현재 오르막 높이, 최대 오르막 높이

    for i in range(1, N):  # 인덱스 에러 방지 위해 i = 1부터 시작
        if road[i - 1] < road[i]:  # 오르막길이라면,
            now_height += road[i] - road[i - 1]  # 현재 높이에 올라간만큼 더하고,
            max_height = max(max_height, now_height)  # 최대 높이 갱신
        else:  # 오르막길이 끝났다면,
            now_height = 0  # 현재 높이 초기화

    print(max_height)