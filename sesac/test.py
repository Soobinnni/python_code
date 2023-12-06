from collections import defaultdict

books = defaultdict(int)

for _ in range(int(input())):
    books[input()] += 1

books = sorted(books.items(), key=lambda x: (-x[1], x[0]))

cnt = -1
ans = ''

for k, v in books:
    if v > cnt:
        cnt = v
        ans = k

print(ans)
#
# books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
#
