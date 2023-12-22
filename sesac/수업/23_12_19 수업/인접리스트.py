V, E = map(int, input().split())

adj_matrix = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input())
    adj_matrix[start].append(end)
    adj_matrix[end].append(start)

for i, am in enumerate(adj_matrix):
    print(f"{i}노드와 연결된 노드: {am}")