for tc in range(1, int(input())+1):
    N = int(input())
    price_flow = list(map(int, input().split()))

    max_p = 0
    profit = 0

    for p in price_flow[::-1]:      # 뒤에서부터 보기!
        if p > max_p:               # 현재 기준보다 크다면 기준 갱신
            max_p = p

        else:                       # 아니라면 그 날 사서 기준일에 팔아서 이득보기
            profit += max_p - p

    print(f'#{tc} {profit}')