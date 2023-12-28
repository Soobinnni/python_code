# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# matching = list(enumerate(map(int, input().split())))  # enumerate 함수 사용하여 (참가번호, 가위바위보) 형태로 저장

# 1은 가위, 2는 바위, 3은 보
# 1-2 = 2 / 1-3 = 1 / 2-3 = 3
# 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자
# array: (index, card)

def game(me, you):
    if (me[1] - you[1]) % 3 == 1:
        return True
    elif (me[1] - you[1]) % 3 == 2:
        return False
    elif me[0] > you[0]:
        return False
    else:
        return True

def game_result(array):
    n = len(array)
    if n == 1:
        return array[0]
    # if n == 2:
    #     if game(array[0], array[1]):
    #         return array[0]
    #     else:
    #         return array[1]

    x = game_result(array[: n // 2 + 1])
    y = game_result(array[n // 2 + 1:])
    if game(x,y):
        return x
    else:
        return y

def main():
    T = int(input())
    for test_case in range(1, T+1):
        N = int(input())

        array = list(zip(range(1, N+1),map(int, input().split())))

        print(f"#{test_case} {game_result(array)[0]}")
main()