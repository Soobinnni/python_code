# https://school.programmers.co.kr/learn/courses/30/lessons/181836

def solution(picture, k):
    ans = []
    for pc in picture:
        word = ''
        for p in pc:
            word = word + (p * k)
        for _ in range(k):
            ans.append(word)
    return ans

def solution_2(picture, k):
    ans = []
    for pc in picture:
        for _ in range(k):
            ans.append(pc.replace('x', ('x' * k)).replace('.', ('.' * k)))
    return ans

def solution_3(picture, k):
    return [pc.replace('x', ('x' * k)).replace('.', ('.' * k)) for pc in picture for _ in range(k)]


def solution_4(picture, k):
    ans = []
    for pc in picture:
        ans += [pc.replace('x', ('x' * k)).replace('.', ('.' * k))] * k
    return ans

for a in solution_4([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2):
    print(a)
# result = [
#           "..xxxx......xxxx..",
#           "..xxxx......xxxx..",
#           "xx....xx..xx....xx",
#           "xx....xx..xx....xx",
#           "xx......xx......xx",
#           "xx......xx......xx",
#           "..xx..........xx..",
#           "..xx..........xx..",
#           "....xx......xx....",
#           "....xx......xx....",
#           "......xx..xx......",
#           "......xx..xx......",
#           "........xx........",
#           "........xx........"
#           ]
for a in solution(["x.x", ".x.", "x.x"], 3):
    print(a)
# result = [
#     "xxx...xxx",
#     "xxx...xxx",
#     "xxx...xxx",
#     "...xxx...",
#     "...xxx...",
#     "...xxx...",
#     "xxx...xxx",
#     "xxx...xxx",
#     "xxx...xxx"
# ]
