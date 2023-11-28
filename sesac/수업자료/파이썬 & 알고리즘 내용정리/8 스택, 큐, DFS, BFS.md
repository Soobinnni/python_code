# 스택(Stack)과 DFS & 큐(Queue)와 BFS

<aside>
💡 파이썬에서 스택과 큐는 모두 리스트로 구현합니다.

</aside>

## 스택(Stack) 자료구조

> 후입 선출 자료구조. ex) 총의 탄창, 뒤로가기 버튼 구현 등
> 

스택은 뭔가를 쌓는다는 이미지를 떠올리시면 됩니다. 파이썬에서는 리스트를 활용하여 스택을 구현할 건데, 파이썬 리스트를 90도 회전해서 돌린 이미지를 상상하시면 됩니다.

![Untitled](https://useful-pantry-930.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F953b07d2-a095-4b83-85d4-10e56ff1a79d%2FUntitled.png?table=block&id=da94c92d-3f8f-43c3-be38-89b92f75907e&spaceId=2c73f946-8332-4a01-81d0-e72428bf9af8&width=380&userId=&cache=v2)

💡 스택은 나중에 들어온 데이터가 먼저 빠져나가게 됩니다.

중요한 점은, 데이터의 삽입과 추출이 모두 리스트의 `뒷부분` 에서 일어난다는 것입니다.

**신규 데이터의 삽입은 그러므로 `append()`를 활용하며, 데이터의 추출은 `pop()`을 활용하여 메서드 만드로 자연스럽게 스택 자료구조를 구현할 수 있습니다**.

웹 서핑을 하다가 뒤로 가는 경우를 코드로 구현해 옮겨 보겠습니다.

```python
visits = [] # 방문 기록지
# 1. 처음으로 구글에 방문
visits.append('google') #  ['google']

# 2. 그다음 인스타그램에 방문
visits.append('instagram') # ['google', 'instagram']

# 3. 그다음 페이스북에 방문
visits.append('facebook') # ['google', 'instagram', 'facebook']

# 4. 뒤로가기 버튼을 누름
visits.pop()
print(visits) # ['google', 'instagram'] => 다시 인스타그램 페이지로 돌아옴
```

> class를 활용한 스택의 직접 구현 코드 (참고)
> 

```python
class Stack:
    def __init__(self,n):
        self.top = -1
        self.stack = [0]*n

    def push(self,data):
        if self.top == len(self.stack) - 1:
            return None
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            return None
        self.top -= 1
        return self.stack[self.top+1]

my_stack = Stack(10)
my_stack.push('alex')
print(my_stack)
print(my_stack.pop())
print(my_stack)
```

---

## DFS (Depth First Search, 깊이 우선 탐색)

<aside>
💡 Stack을 활용하여 DFS를 구현할 수 있습니다.

</aside>

1️⃣ 만약 이런 `그래프`(루프가 존재)가 있다고 하면, 파이썬으로는 어떻게 정보를 구조화할 수 있을까요?

우선, 이 동그란 포도알들은 `노드(Node)` 혹은 `Vertex`라고 하며, 파란색 선은 `간선(Edge)`이라고 부릅니다.

![Untitled](https://useful-pantry-930.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbf9c16cc-8053-4a50-a2ea-a3c5c03ac86b%2FUntitled.png?table=block&id=f369ab53-ae98-40e8-8867-e8258b94f90a&spaceId=2c73f946-8332-4a01-81d0-e72428bf9af8&width=1210&userId=&cache=v2)

2️⃣ 아무튼, 이 문제의 초창기 인풋은 이런 식으로 들어오게 됩니다. (단뱡향이면 문제가 알려줌)

```python
7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
1 2  # 다음 8개의 줄에 연결 정보를 제공
1 3
2 4
2 5
4 6
5 6
6 7
3 7
```

3️⃣ 인접 행렬로 정리하기

```python
V, E = map(int, input().split())  # Vertex(포도알), Edge(선) 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀 + 0번 포도알은 안씀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

# adj_matrix print 결과

# [[0, 0, 0, 0, 0, 0, 0, 0],  => 0번 포도알은 존재하지 않음
#  [0, 0, 1, 1, 0, 0, 0, 0],  => 1번 포도알은 2, 3번으로 갈 수 있음
#  [0, 1, 0, 0, 1, 1, 0, 0],  => 2번 포도알은 1, 4, 5번 가능
#  [0, 1, 0, 0, 0, 0, 0, 1],  => 3번 포도알은 1, 7번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 4번 포도알은 2, 6번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 5번 포도알은 2, 6번 가능
#  [0, 0, 0, 0, 1, 1, 0, 1],  => 6번 포도알은 4, 5, 7번 가능
#  [0, 0, 0, 1, 0, 0, 1, 0]]  => 7번 포도알은 3, 6번 가능
```

4️⃣ 인접 리스트로 정리하기

```python
V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향

# adj_list = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
```

정리하자면, 노드와 간선의 연결 정보를 정리하는 방법은 `인접 행렬`과 `인접 리스트` 두 가지가 있고,

DFS 문제풀이 방식은 `Stack`을 이용하는 방법과 `재귀 함수`를 이용하는 방식 두 가지로 나뉩니다.

그러니 정보 정리 방법 2가지 X 풀이방법 2가지를 섞으면 총 4개의 풀이법이 나옵니다.

1. 스택 + 인접 행렬
2. 스택 + 인접 리스트
3. 재귀 + 인접 행렬
4. 재귀 + 인접 리스트

다만, 어떤 방식으로 풀든간에 `visited` 개념은 꼭 필요합니다.

⇒ 방문한거 계속 스택에 집어넣거나 재귀 돌리면 무한루프 걸리거든요.

5️⃣ 그렇다면 Stack을 왜 쓰는거고 이게 왜 `깊이`우선 탐색이지?

```python
# 최초 시행
visited = []
stack = [1]

# stack pop => 1 후에 갈 수 있는걸 골라보니? 2, 3번 포도알로 갈 수 있었음.
visited = [1]
stack = [2, 3] 

# 그런 다음 다음 pop은 stack이니까 뒤부터 3이 튀어나옴 + 3이 갈 수 있는 7이 더해짐.
visited = [1, 3]
stack = [2, 7]  # 1은 visited에 있으니까 안들어감

# 7을 뽑아냄
visited = [1, 3, 7]
stack = [2, 6]

# 이런식으로 2는 계속 기다리고, 3 -> 7 -> 6 식으로 쭉쭉 "깊게" 뻗어나감!
```

6️⃣ DFS 풀이방법 정리

> **스택 + 인접 행렬** (공간 복잡도 높으나, 단방향 그래프인 경우 전치로 방향 전환 유리)
> 

```python
V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while stack:  # 스택이 빌때까지 돌아라!
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌
		
		# 위의 if문 안으로 넣으면 더 좋습니다.
    for destination in range(V+1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장

print('이동경로:', *visited)

# 이동경로: 1 3 7 6 5 2 4
```

> **스택 + 인접 리스트** (공간 복잡도 낮음)
> 

```python
V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_list = [[] for _ in range(V + 1)]  # 인접리스트 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while stack:  # 스택이 빌때까지 돌아라!
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in adj_list[current]:
        if destination not in visited:  # 갈 수 있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장

print('이동경로:', *visited)

# 이동경로: 1 3 7 6 5 2 4
```

> **재귀 + 인접 행렬** (가독성은 좋으나 재귀 자체가 좀 느림)
> 

`주의`: 재귀함수를 활용하는 경우 return을 쓰면 끊길 수 있으므로 조심합니다.

```python
def dfs(n):
    if n not in visited:  # 우선 visited 없으면 넣어줌
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)  # 다음 재귀 깊이로 이동

V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

visited = []  # 궤적 기록용

dfs(1)  # 1번 포도알부터 시작!

print('이동경로:', *visited)

# 이동경로: 1 2 4 6 5 7 3 => 이거 다른거 주의!!
# main이 종료되어야 sub가 실행된다는 것을 생각
# 다음 main은 이전 main의 sub임
# (main) (sub1) (sub2) ...
# 1
# 1-2 / 1-3
# 1-2-4 / 1-2-5 / 1-3
# 1-2-4-6 / 1-2-4-5 / 1-2-5 / 1-3
# 1-2-4-6-5 / 1-2-4-6-7 / 1-3 # main이 5를 갔으니 sub 1-2-5, sub 1-2-4-5는 시작도 못함
# (1-2-4-6-5) / 1-2-4-6-7 / 1-3 # main 종료 및 기록됨, 이전 main 1-2-4-6이 main이 됨
# (1-2-4-6-5)-7 / 1-3 # main이 7을 갔으니 sub 1-2-4-6-7은 시작도 못함
# (1-2-4-6-5)-7-3 # main이 3을 갔으니 sub 1-3은 시작도 못함
# main 종료, sub는 없음
```

💡 일반적으로 재귀함수를 이용한 DFS는 미로찾기 등의 문제에서 가로 * 세로가 12 X 12 이상이 되면 `maximum recursion depth 에러` 가 뜰 수 있으므로 지양합니다. 그러므로 DFS 문제는 `Stack`
을 활용하여 푸는 방식이 좋습니다.

> DFS 연습문제 => 연속한 1의 갯수 찾기 ⇒ 델타 탐색을 응용합니다.
> 

```python
# N*N크기의 배열이 주어졌을때 1의 개수는 몇개인지 세어보기 dfs를 이용해서
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수 세어보기 => 2, 13이 답이 됨.
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000
# 방향잡기(상,우,하,좌)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 행과 열의 좌표가 들어옴
def DFS(r, c):
    global cnt
    # 해당 arr[r][c] 자리값이 1이므로 방문체크와 동시에 카운트를 1증가
    arr[r][c] = 0
    cnt += 1
    # 4방 탐색
    for i in range(4):
        # 새로운 좌표값을 활용
        nr = r + dr[i]
        nc = c + dc[i]

        # 새로운 좌표값을 활용한 범위검사
        # 범위를 벗어나면 다른 방향을 탐색
        # if 0<=nr<N and 0<=nc<N: 조건도 가능(파이썬에서만)
        if nr<0 or nr>= N or nc <0 or nc>=N:
            continue
        # 이미 방문을 했어도 종료(이것이 없으면 무한으로 방문)
        # 이 아래 조건을 위에 한꺼번에 쓸거면 단축평가 오른쪽엔 가능함 근데 이거 따로쓸거면 맵 제한조건보다 위에 두면 조짐. 
        if arr[nr][nc] == 0:
            continue
        # 걸러낼 조건을 모두 걸러내면 재귀가 가능
        DFS(nr, nc)  # 또 한 뎁스 들어가라!!

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]  # 행의 길이만큼 만들어준다

# 입력이 끝났으면 처음 시작 위치 찾기
for i in range(N):  # 행우선순회 하면서 전부다 보되
    for j in range(N):
        if arr[i][j] == 1:  # 그자리가 1이야?
            cnt = 0  # prep 하고
            DFS(i, j)  # dfs 해!
            print(cnt)
```

- 추가 참고코드
    
    ```python
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    def BFS(r, c):
        # Q를 초기화
        Q = []
        Q.append((r, c))
        dist[r][c] = 1
        # Q에 요소가 존재할때까지만 돌 것(빈 컨테이너가 되면 멈춰버린다)
        while Q:
            curr_r, curr_c = Q.pop(0)
            # 4방향탐색
            for i in range(4):
                nr = curr_r + dr[i]
                nc = curr_c + dc[i]
                # 범위를 벗어나면 다른방향 탐색
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                # 갈 수 없는 자리거나 이미 방문한 경우
                if arr[nr][nc] == 0 or dist[nr][nc] != 0: continue
    
                Q.append((nr, nc))
                dist[nr][nc] = dist[curr_r][curr_c] + 1
    
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]  # 행의 길이만큼 만들어준다
    dist = [[0]*N for _ in range(N)]
    # 입력이 끝났으면 처음 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and dist[i][j] == 0:
                BFS(i, j)
    
    for d in dist: # 이 부분을 프린트해서 찍어봅니다!
        print(*d)
    
    # 7
    # 0000011
    # 0000000
    # 0011100
    # 0010111
    # 0110010
    # 0011100
    # 0000000
    ```
    

---

## 큐(Queue) 자료구조

> 선입 선출 자료구조. ex) 식당의 대기줄, 편의점 재고
> 

사람들이 이렇게 줄을 서 있는 경우를 생각해 봅시다. 

![Untitled](https://useful-pantry-930.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3b436a82-420c-4e8c-8101-5992f755748d%2FUntitled.png?table=block&id=6693351c-e385-4887-91ab-f3cb609529a4&spaceId=2c73f946-8332-4a01-81d0-e72428bf9af8&width=1740&userId=&cache=v2)

스택과 비슷하게, 큐는 앞쪽부터 자료가 빠져나가며 삽입은 리스트 뒤로 이어지게 됩니다.

```python
people = ['april', 'jane', 'bob', 'brad']

# 줄이 줄어든다면? => 앞쪽부터 빠져나간 것!
people.pop(0)
print(people) # ['jane', 'bob', 'brad']

# 줄에 사람이 추가된 경우?
people.append('kelly')
print(people) # ['jane', 'bob', 'brad', 'kelly']

# 중간에 추가된 경우나, 인원이 나가는 경우도 슬라이싱 삽입이나 insert 등으로 구현 가능합니다.
```

## BFS (Breath First Search, 너비 우선 탐색)

<aside>
💡 Queue를 활용하여 BFS를 구현할 수 있습니다.

</aside>

> 💡 너비 우선 탐색 ⇒ Queue 활용!
> 

> 큐의 특성상 앞에서부터 빠지므로? 거리에 따른 등고선 형태가 됩니다.
![Untitled](https://useful-pantry-930.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F48c18d0a-c147-4443-beca-0091498f89e0%2FUntitled.png?table=block&id=64494791-1106-4ac9-a1c1-2163e40d89a5&spaceId=2c73f946-8332-4a01-81d0-e72428bf9af8&width=1230&userId=&cache=v2)

```python
V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

Q = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while Q:  # 큐가 빌때까지 돌아라!
    current = Q.pop(0)  # 우선 큐에서 현재 위치 "앞에서부터" 뽑고,
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in range(V+1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
            Q.append(destination) # 다음 갈 곳으로 큐에 저장

print('이동경로:', *visited)

# 이동경로: 1 2 3 4 5 7 6
```