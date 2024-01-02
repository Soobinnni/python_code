quizes = [input() for _ in range(int(input()))]

for quize in quizes:
    score = ans = 0
    for q in quize:
        if q == 'O':
            score += 1
            ans += score
        else:
            score = 0

    print(ans)