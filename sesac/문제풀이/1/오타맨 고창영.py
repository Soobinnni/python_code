for _ in range(int(input())):
    idx, word = input().split()
    word = list(word)
    word.pop(int(idx)-1)
    print(''.join(word))