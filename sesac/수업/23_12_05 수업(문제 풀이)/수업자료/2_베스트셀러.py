import sys
input = sys.stdin.readline

from collections import defaultdict

books_sales_info = defaultdict(int)

for _ in range(int(input())):
    books_sales_info[input().rstrip()] += 1 # 키값 선언 없이 바로 연산

books_names = sorted(books_sales_info)

cnt = -1
ans = ''

for book_name in books_names:
    if books_sales_info[book_name] > cnt:
        cnt = books_sales_info[book_name]
        ans = book_name

print(ans)