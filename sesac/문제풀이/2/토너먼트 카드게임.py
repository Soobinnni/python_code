def game(player1, player2):
    game_result = player1[1] - player2[1]
    if not game_result:
        return player1 if player1[0] < player2[0] else player2
    if game_result in (-2, 1):
        return player1
    else:
        return player2

def tournament(team):
    if len(team) == 1:
        return team[0]
    else:
        l = tournament(team[:(len(team)+1) // 2])
        r = tournament(team[(len(team)+1) // 2:])
        return game(l, r)


for test_case in range(1, int(input()) + 1):
    n = int(input())
    people_card = list(enumerate(map(int, input().split())))
    winner = tournament(people_card)[0]+1

    print(f"#{test_case} {winner}")



