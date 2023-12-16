def find(idx, w):
    global ans
    start = l = idx
    end = r = (m-1) + idx
    while l<r:
        if w[l] == w[r]:
            l += 1
            r -= 1
        else:
            return False
    ans = ''.join(w[start:end+1])
    return

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    column_words = list(map(list, zip(*words)))

    ans = ''
    integral = n-m+1

    for i in range(n):
        for j in range(integral):
            if find(j, words[i]) or find(j, column_words[i]): break
    print(f'#{test_case} {ans}')