encyclopedia_num, quize_num = map(int, input().split())

pocketmons = [input() for _ in range(encyclopedia_num)]
quizes = [input() for _ in range(quize_num)]

for q in quizes:
    print(pocketmons[int(q)-1]) if q.isdigit() else print(pocketmons.index(q) + 1)