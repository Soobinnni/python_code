def solution(): # 내 최종 답변
    words = [input() for _ in range(int(input()))]
    cnt = 0

    for word in words:
        copy_word = word
        for i in range(1, len(word)):
            if word[i - 1] == word[i]: copy_word = copy_word.replace(word[i], '', 1)

        if len(copy_word) == len(set(word)): cnt += 1
    print(cnt)

def solution2(): # visited 활용
    ans = 0

    for _ in range(int(input())):
        word = input().rstrip()

        visited = set(word[0])  # 방문지에 단어의 첫 문자를 넣고 출발

        for i in range(1, len(word)):  # 두번째 문자부터 검토

            if word[i] != word[i - 1] and word[i] in visited:  # 바로 앞 문자와 다르면서 이미 방문한 문자인 경우
                break  # 그룹 단어가 아님

            elif word[i] not in visited:  # 새로운 문자가 나타난 경우
                visited.add(word[i])  # 방문지에 추가

        else:  # 마지막 문자까지 통과하면 정답 +1
            ans += 1

    print(ans)

def solution3(): # Counter 메서드 활용
    from collections import Counter

    ans = 0

    for _ in range(int(input())):
        word = input().rstrip()
        letter_cnt = Counter(word)  # 각 문자가 총 몇 번 나오는지 기록

        for letter, cnt in letter_cnt.items():  # 각 문자와 그 문자가 나온 횟수를 뽑아
            if (letter * cnt) not in word:  # 해당 횟수만큼 연속해서 나온 적이 없다면
                break  # 그룹 단어가 아님
        else:  # 모든 검사를 통과했다면
            ans += 1  # 정답 +1

    print(ans)