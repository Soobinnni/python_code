# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
def get_min_production_cost(depth, acc):
    global ans
    if depth == N:
        if acc < ans: ans = acc
        return

    for i in range(N):
        temp_acc = acc + costs[depth][i]
        if (not check[i]) and (temp_acc < ans):
            check[i] = 1
            get_min_production_cost(depth + 1, temp_acc)
            check[i] = 0

for test_case in range(1, int(input())+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    ans = 99999999

    get_min_production_cost(0, 0)
    print(f"#{test_case} {ans}")