# https://www.acmicpc.net/problem/2606
V = int(input()) # 노드 개수
E = int(input()) # 간선 개수
matrix = [[] for _ in range(V+1)]

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
# 인접 리스트
for i in range(E):
    start, end = map(int, input().split())
    matrix[start].append(end)
    matrix[end].append(start)

stack = [1]
visited = set()

while stack:
    curr = stack.pop()
    if curr not in visited:
        visited.add(curr)

    for destination in range(V+1):
        if destination in matrix[curr] and destination not in visited:
            stack.append(destination)

print(len(visited)-1)