# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    ans = []
    for q in quiz:
        Q, num = q.split(' = ')
        ans.append('O' if eval(Q) == int(num) else 'X')
    return ans

test_case1 = ["3 - 4 = -3", "5 + 6 = 11"]	# result = ["X", "O"]
test_case2 = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	# result = ["O", "O", "X", "O"]

print(solution(test_case1))
print(solution(test_case2))