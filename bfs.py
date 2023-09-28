# queue 자료구조를 사용해서 적용
from collections import deque # deque 라이브러리 import

def bfs(graph, start, visited):
    queue = deque([start]) # queue 생성
    visited[start] = True # 처음 경로 저장
    while queue:
        v = queue.popleft() # 처음 들어간 걸 꺼내고
        print(v, end=' ') # 기록하고
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # queue 에 넣고
                visited[i] = True # 방문 처리 하고

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
] 
visited = [False] * 9
bfs(graph, 1, visited)