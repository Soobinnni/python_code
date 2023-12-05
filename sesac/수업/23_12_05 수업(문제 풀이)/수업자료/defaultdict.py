from collections import defaultdict

my_dict1 = defaultdict(int)
my_dict2 = defaultdict(str)
my_dict3 = defaultdict(list)
my_dict4 = defaultdict(set)

# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)

# 디폴트값
# print(my_dict1['my_key'])
# print(my_dict2['my_key'])
# print(my_dict3['my_key'])
# print(my_dict4['my_key'])
# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)

# 키 에라
# my_dict5 = dict()
# print(my_dict5['my_key'])

# 활용하기
# my_dict1['my_key'] += 1
# print(my_dict1)
# print(my_dict1['my_key'])
# my_dict3['my_key'].append(1)
# print(my_dict3)
# print(my_dict3['my_key'])

# 딕셔너리 정렬
# my_dict6 = {'c':5, 'a':5, 'b':3, 'e':4, 'd':3}
# # my_dict6.sort()
# print(sorted(my_dict6))
# print(sorted(my_dict6.items()))
# print(dict(sorted(my_dict6.items())))
# print(sorted(my_dict6.items(), key=lambda x : x[1]))