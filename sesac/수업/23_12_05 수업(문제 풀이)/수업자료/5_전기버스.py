for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    charges = set(map(int, input().split()))

    location = K
    ans = 0

    while location < N:
        for i in range(location, location - K, -1): # 뒤에서부터 검사
            if i in charges:                        # 범위 내에 충전소가 있으면
                ans += 1                            # 충전하고
                location = i                        # 이동
                break
        else:                                       # for - else, 범위 내에 충전소가 없으면
            ans = 0                                 # 정답 0으로 초기화
            break

        location += K

    print(f'#{tc} {ans}')