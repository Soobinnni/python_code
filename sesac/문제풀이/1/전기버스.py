T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())

    # K가 N보다 크면
    if K > N:
        count = 0
        print(f"#{test_case} {count}")
        break

    charge_stations = list(map(int, input().split()))
    stations = [True if i in charge_stations else False for i in range(N+1)]

    count = 0
    current_station = 0

    for _ in range(M):
        integral = stations[current_station : current_station+K+1]
        if True not in integral:
            count = 0
            break

        index = integral[::-1].index(True)

        # k와 index가 같을 경우, 시작점이 충전지이므로 예외. 그러나 종착지에 도착할 수 있다면 또 제외.
        if index == K and (current_station + K != N):
            count = 0
            break
        current_station = (len(integral) - index - 1) + ( K * count )
        count +=1

        if (current_station + K) >= len(stations)-1:
            break

    print(f"#{test_case} {count}")