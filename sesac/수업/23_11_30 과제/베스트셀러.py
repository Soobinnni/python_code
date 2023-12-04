count = int(input())
books = {}
for _ in range(count):
    book= input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
best_sell_count = max(books.values())
best_seller = []
for k, v in books.items():
    if v == best_sell_count:
        best_seller.append(k)
best_seller.sort()
print(best_seller[0])