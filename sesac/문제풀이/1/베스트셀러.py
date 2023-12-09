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

# defaultdict
#   모듈 -> from collections import dictdict
#   선언
#   my_dict = defaultdict(value의 class)
#   예) my_dict1 = defaultdict(int)
#      my_dict2 = defaultdict(str)
#      my_dict3 = defaultdict(list)
#      my_dict4 = defaultdict(set)
#       print(my_dict1) >> defaultdict(<class 'int'>, {})

# defaultdict는 key에러를 방지한다.
#   print(my_dict1['my_key']) >> key가 없지만, 결과는 0(int의 초기값) 
#   print(my_dict2['my_key']) >> key가 없지만, 결과는 ''(int의 초기값) 
#   print(my_dict3['my_key']) >> key가 없지만, 결과는 list()(int의 초기값) 
#   print(my_dict4['my_key']) >> key가 없지만, 결과는 set()(int의 초기값) 
# 이후, my_key key로 value에 초기값이 들어감


for _ in range(count):
    book= input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

# 이 문장을 효율적으로 수정 가능.
from collections import defaultdict
books = defaultdict(int)
for _ in range(count):
    book = input()
    books[book].append


# ------sort방법 -> value가 기준이 되어야 한다.
# sort메서드는 불가능하지만 sorted함수는 dictionary에 적용할 수 있다.
# sorted(dictionary) -> key값만 정렬 [a,b,c,d,e]
# sorted(dict.itmes()) -> 튜플 형태로 반환되며 k 를 기준으로 정렬{예: [(a,1), (b,3), (c,3), (d,1), (e,1)]
# dict(sorted(dict.itmes())) -> 튜플 형태 대신, k-v의 dict로 반환 {'a':1, 'b':3, 'c':3, .. }

# 해결방법 : sorted함수와 key = lambda
# books_sales_info = sorted(books_sales_info.items(), key = lambda x: (-x[1], x[0])) -> [(b,3), (c,3), (a,1), (d,1), (e,1)]