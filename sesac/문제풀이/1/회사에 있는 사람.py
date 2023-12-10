in_company = { x[0]:x[1] for x in (input().split() for _ in range(int(input())))}
ans = sorted([k for k,v in in_company.items() if v == 'enter'], reverse=True)

for a in ans:
    print(a)