def dfs(cur):
    if cur not in visited: visited.append(cur)

    for destination in adj_matrix[cur]:
        if destination not in visited: dfs(destination)

V, E = map(int, input().split())

adj_matrix = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start].append(end)
    adj_matrix[end].append(start)

visited = []
dfs(1)

print(f"탐색 순서: {visited}")