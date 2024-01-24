# https://school.programmers.co.kr/learn/courses/30/lessons/181837

def solution(order):
    return (4500 * len(order)) + sum(500 for o in order if "cafelatte" in o)

print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"])) # result = 19000
print(solution(["americanoice", "americano", "iceamericano"])) # result = 13500