num = int(input())

for i in range(1, num+1):
    print((' *'*num).rstrip() if i % 2 == 0 else ('* '*num).rstrip())