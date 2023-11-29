a = [1,2,3]
b = [1,2,3]
c = a

print(a,b,c)
print(id(a), id(b), id(c))

a[0] = 9
print(a,b,c)