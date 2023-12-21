V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(V+1):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = []
Q = [1]

while Q:
    cur = Q.pop(0)
    if cur not in visited: visited.append(cur)

    for destination in range(V+1):
        if adj_matrix[cur][destination] and destination not in visited: Q.append(destination)

print(f"탐색 순서: {visited}")