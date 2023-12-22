# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7

V, E = map(int, input().split())

# 인접 행렬
# adj_matrix = [[0] * (V+1) for _ in range(V+1)]
#
# for _ in range(V+1):
#     start, end = map(int, input().split())
#     adj_matrix[start][end] = 1
#     adj_matrix[end][start] = 1

# 인접 리스트
adj_matrix = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())

    adj_matrix[start].append(end)
    adj_matrix[end].append(start)

visited = []
stack = [1]

while stack:
    cur = stack.pop()

    if cur not in visited: visited.append(cur)

    # # 인접 행렬
    # for destination in range(V+1):
    #     if destination not in visited and adj_matrix[cur][destination]:
    #         stack.append(destination)

    # 인접 리스트
    for destination in adj_matrix[cur]:
        if destination not in visited: stack.append(destination)

print(visited)