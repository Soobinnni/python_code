# https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    dif_arr = [abs(n - a) for a in array]
    min_dif = min(dif_arr)
    ans = []
    for a in array:
        if abs(n - a) == min_dif:
            ans.append(a)

    return sorted(ans)[0]

def solution_2(array, n):
    return sorted([a for a in array], key = lambda x:(abs(n-x), x))[0]

print(solution([3, 10, 28], 20)) # result = 28
print(solution([10, 11, 12], 13)) # result = 12