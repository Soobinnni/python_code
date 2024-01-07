# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN
for test_case in range(1, int(input())+1):
    bit = list(map(int, input()))
    initial = [0] * len(bit)
    cnt = 0

    for i in range(len(bit)):
        if bit[i] != initial[i]:
            change = int(not bool(initial[i]))
            for j in range(i, len(bit)):
                initial[j] = change
            cnt += 1

        if bit == initial:
            break


    print(f"#{test_case} {cnt}")