# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    ans = []
    N = len(score)
    for i in range(N):
        grade = N
        for j in range(N):
            if i == j: continue
            if sum(score[j]) <= sum(score[i]):
                grade -= 1

        ans.append(grade)
    return ans

# 다른 사람 코드
def solution_2(score):
    sum_score = [sum(s) for s in score]
    arr = sorted(sum_score, reverse=True)
    return [arr.index(s) + 1 for s in sum_score]

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]])) # result = [1, 2, 4, 3]
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])) # result = [4, 4, 6, 2, 2, 1, 7]