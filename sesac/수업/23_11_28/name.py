# a = [1,2,3,4]
# b = [1,2,3,4]
#
# a == b >> True
# a is b >> False
#
# id(a) != id(b)이기 때문에
# (정확히는 아니지만, id는 메모리 주소를 지칭)

a = [1,2,3]
b = [1,2,3]
c = a

print(a,b,c)
print(id(a), id(b), id(c))

a[0] = 9
print(a,b,c)