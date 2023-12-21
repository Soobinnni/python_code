def dfs(cur):
    if cur not in visited:
        visited.append(cur)

    for destination in range(V + 1):
        if adj_matrix[cur][destination] and destination not in visited:
            dfs(destination)

V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(V+1):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = []
dfs(1)

print(f"탐색 순서: {visited}")