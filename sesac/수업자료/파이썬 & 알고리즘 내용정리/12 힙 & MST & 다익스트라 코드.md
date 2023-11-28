<aside>
💡 SWEA 5249, 5251 문제를 읽고 보면 좋습니다.

</aside>

## 힙 자료구조

```python
heap = ['최소힙:']

def heap_push(item):
    heap.append(item)  # 1. 일단 맨 끝에 넣는다

    child = len(heap) - 1  # 자기자신은 방금 붙인 걔
    parent = child // 2  # 부모는 반토막 index

    # 루트 노드가 아닌 한 + 최소힙이지만 부모가 크다면 바꿔야하니까?
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # 스왑
        child = parent  # 이제 아이가 부모가 되고
        parent = child // 2  # 부모는 아이 index의 반토막

def heap_pop():
    if len(heap) == 1:
        print('힙이 비어있어 삭제가 불가능합니다!')
        return

    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    parent = 1
    child = parent * 2  # 일단 좌측 child 기준으로 잡고

    if child+1 <= len(heap)-1:  # 우측이 트리상에서 존재하는 경우 +
        if heap[child] > heap[child+1]:  # 좌측이 우측보다 더 큰 경우
            child += 1  # 우측 자식 기준으로 자식의 자격을 바꿈
            # 왜냐면 자리 바꿀때 더 작은 값이 최소힙의 경우 우선순위가 높아서
            
    while child <= len(heap)-1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    return result

heap_push(33)
print(heap)
heap_push(12)
print(heap)
heap_push(7)
heap_push(19)
heap_push(21)
print(heap)
heap_push(5)
print(heap)
heap_push(8)
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
```

- ver2.
    
    ```python
    heap = ['최소힙 :']
    
    def heap_push(item):
        heap.append(item)  # 완전 이진트리니까 맨끝에 +
    
        child = len(heap)-1
        parent = child // 2
        # 루트노드가 아니고, 위에 봤는데 더 큰 경우 계속 돎
        while parent and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]  # swap
            child = parent
            parent = child // 2
    
    def heap_pop():
         if len(heap) == 1:
            print('힙이 비어있어 삭제가 불가능합니다!')
            return
    
        result = heap[1]
        heap[1] = heap[-1]
        heap.pop()
    
        parent = 1  # 루트부터 시작하니까 1
        child = parent * 2  # 일단 왼쪽이 작다고 가정하자
    
        # 이번에는 아래로 내려가는거니까 오른쪽 노드가 존재할때까지 +
        # 최소힙 유지를 위해 필요할때까지!
        while child <= len(heap)-1 and heap[parent] > heap[child]:
            if child+1 <= len(heap)-1:  # 오른쪽 노드가 트리 안에 존재하고 +
                if heap[child] > heap[child+1]:  # 왼쪽이 더 크면 최소힙으로서는
                    child += 1  # 오른쪽으로 내려가야하는게 맞음
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child  # 이번에는 내려가는거니까 반대
            child = parent * 2  # 일단 이번에도 왼쪽이라고 가정해봄
    
        return result
    
    heap_push(33)
    print(heap)
    heap_push(12)
    print(heap)
    heap_push(7)
    heap_push(19)
    heap_push(21)
    print(heap)
    heap_push(5)
    print(heap)
    heap_push(8)
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    print(heap_pop())
    print(heap)
    ```
    

## MST

> **크루스칼**
> 

`1` 기본 Union 코드

```python
# SWEA 5249 최소신장트리 풀이
T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):  # 효율성이 고려된 find set
    if p[x] != x:
        p[x] = find_set(p[x])  # path compression
    return p[x]

def union(x, y):  # 랭크가 고려 안된 union
    p[find_set(y)] = find_set(x)

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])  # 가중치 오름차순 정렬
    p = [0]*(V+1)  # 0 ~ V 번까지 있으니까 V+1 개
    for i in range(V+1):
        make_set(i)  # list(range(V+1))과 같음

    answer = 0  # 가중치 합산 모아줄 변수
    cnt = 0  # 간선 선택 횟수

    for x, y, w in edges:  # 대표자 같으면 다음으로 걍 넘어감
        if find_set(x) != find_set(y):  # 대표자가 다른경우에만
            union(x, y)  # union 해주고
            answer += w  # 간선의 가중치를 합산
            cnt += 1  # 간선을 하나 사용했다고 체크

        if cnt == V:  # V-1 개까지만 선택해야 하니까!
            break

    print('#{} {}'.format(tc, answer))

```

`2` 랭크를 고려한 크루스칼

```python
T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):  # 효율성이 고려된 find set
    if p[x] != x:
        p[x] = find_set(p[x])  # path compression
    return p[x]

def union(x, y):  # Union 그룹 합치기 -> 그룹내 모든 값 바꿈
    link(find_set(x), find_set(y))  # 대표끼리 링크!

def link(x, y):  # 랭크가 다른 트리 합치는 것
    if r[x] > r[y]:  # x 쪽 랭크가 큰 경우에는
        p[y] = x  # y를 x에 흡수시킴
    else:
        p[x] = y  # 아닌 경우는 반대긴 한데
        if r[x] == r[y]:  # 같으면?
            r[y] += 1  # y 랭크를 하나 올려줌

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])  # 가중치 오름차순 정렬
    p = [0]*(V+1)  # 0 ~ V 번까지 있으니까 V+1 개
    r = [0]*(V+1)  # 랭크 표시용

    for i in range(V+1):
        make_set(i)  # list(range(V+1))과 같음

    answer = 0  # 가중치 합산 모아줄 변수
    cnt = 0  # 간선 선택 횟수

    for x, y, w in edges:  # 대표자 같으면 다음으로 걍 넘어감
        if find_set(x) != find_set(y):  # 대표자가 다른경우에만
            union(x, y)  # union 해주고
            answer += w  # 간선의 가중치를 합산
            cnt += 1

        if cnt == V:  # V-1 개까지만 선택해야 하니까!
            break

    print('#{} {}'.format(tc, answer))
```

- 합산
    
    ```python
    T = int(input())
    
    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x]) # path compression
        return p[x]
    
    def union(x, y):
        if r[x] > r[y]:
            p[y] = x
        else:
            p[x] = y
            if r[x] == r[y]:
                r[y] += 1
    
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(E)]
        edges.sort(key=lambda x: (x[2]))
        p = list(range(V+1))
        r = [0] * (V+1)
        answer = 0
        cnt = 0
    
        for s, e, w in edges:
            if find_set(s) != find_set(e):
                union(find_set(s), find_set(e))
                answer += w
                cnt += 1
    
            if cnt == V:
                break
    
        print(f'#{tc} {answer}')
    ```
    

> 프림
> 

```python
# SWEA 5249 최소신장트리 풀이
def Prim():
    dist = [987654321] * (V+1)
    dist[V] = 0
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 갱신!

        visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
        # 요거 주석 풀어서 visted, dist 찍어볼것!
        # print(visited, dist)

        # 이제 그 선택된 점에서부터 갈 수 있되, 더 짧은 거리를 보장한다면 dist 배열 갱신
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)  # 마지막에 dist 배열의 총합산이 MST를 이루는 간선들의 합

for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, Prim()))
```

## 다익스트라 알고리즘(dijkstra)

> 최소 비용 및 이동거리를 계산하는 알고리즘입니다.
> 

`1` 리스트 갱신 Ver

```python
# SWEA 5251 최소 이동 거리 풀이

def dijkstra():
    dist = [987654321] * (V+1)
    dist[0] = 0  # 여기 start 점을 넣어주면 됨.
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 갱신!

        visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
        # 요거 주석 풀어서 visted, dist 찍어볼것!
        # print(visited, dist)

        # 이제 그 선택된 점에서부터 갈 수 있되, 그 가중치를 더하더라도 더 짧음을 보장한다면 dist 배열 갱신
        for i in range(V+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[V]  # 도착점

for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))

```

`2` 힙큐 모듈 활용 Ver

> 힙큐 모듈이란?
> 

```python
import heapq  # 힙큐 모듈은 '최소힙'이다!

# 일반적인 잡 리스트를 힙으로 만들어버리기 => 원본을 바꿔버린다는 게 포인트
arr = [2, 4, 7, 3, 5, 8]
heapq.heapify(arr)
print('#1 힙으로 만들기', arr)  # [2, 3, 7, 4, 5, 8]
print('------------------------------------')

# 힙 푸시
print('#2 힙푸시')
heap = []
heapq.heappush(heap, 8)  # 리턴값이 없어서 None임
print(heap)
heapq.heappush(heap, 5)
print(heap)
heapq.heappush(heap, 3)
print(heap)
heapq.heappush(heap, 6)
print(heap)
print('------------------------------------')

# 힙팝
print('#3 힙팝')
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
res = heapq.heappop(heap)
print(heap)
# 없는 상태에서 뽑으려면 index out of range가 난다!
# heapq.heappop(heap)
print('res에 담김: ', res)
print('------------------------------------')

# 힙에는 그럼 숫자만 넘길수있나?
print('#4 튜플 넘기기')
min_heap = []
heapq.heappush(min_heap, (3, 5))  # '앞쪽' 숫자를 기준으로 최소힙을 만든다!
heapq.heappush(min_heap, (1, 6))
heapq.heappush(min_heap, (4, 'hihi'))  # 그러니까 앞에만 숫자이면 됨
# heapq.heappush(min_heap, ('그러니까 이건 오류남', 'hihi'))
print(min_heap)
print('------------------------------------')

# 그러면 최대힙은 어떻게 할건데? => 앞쪽을 기준으로 최소힙을 만든다는 점을 활용
# (내가 구하고자 하는 값의 -를 줘서 우선순위가 거꾸로 하게 함, 진짜 내가 활용하고 싶은 숫자)
print('#5 최대힙')
max_heap = []
heapq.heappush(max_heap, (-3, 3))
heapq.heappush(max_heap, (-5, 5))
heapq.heappush(max_heap, (-4, 4))
print(max_heap)
```

> 힙큐 다익스트라 코드
```python
# SWEA 5251 최소 이동 거리 풀이
import heapq


def dijkstra():
    dist = [987654321] * (V+1)
    visited = set()  # 효율화를 위한 셋
    heap = []  # 빈 리스트 하나 생성해서 최소힙 자료구조로 활용
    heapq.heappush(heap, (0, 0))  # (거리, 노드번호)

    while heap:  # 힙이 빌때까지 돌아라
        distance, node = heapq.heappop(heap)  # 거리와 노드번호를 뽑고 (뽑힌 순간 최소 거리로 뽑혔을 것)
        if node not in visited:  # visited 없는 경우에 한해서 + visited 되지 않은 경우는 바로 다음 힙팝이 실행될 것!
            dist[node] = distance  # 최소힙에서 뽑았으니까 바로 그녀석의 distance가 최소 이동 거리일것
            visited.add(node)  # visited 도장을 찍어준다
	
            for destination in range(V+1):  # 현재의 node에서 갈 수 있는 destination을 모두 체크할건데,
                # 아직 방문하지 않았어야 함과 동시에
                # 목적지까지의 기존 이동거리라고 생각했던 것 > 내 위치까지의 이동거리 + 내 위치로부터 목적지까지의 이동거리를 만족하면
                if destination not in visited and dist[destination] > adj[node][destination] + dist[node]:
                    heapq.heappush(heap, (adj[node][destination] + dist[node], destination))  # 최소힙에 넣어라!

    return dist[V]


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))

```