# stack 자료구조를 사용, 재귀함수 이용
# 깊이 우선 탐색

def dfs(graph, v, visited): 
    visited[v] = True # 방문 처리
    print(v, end=' ') # 방문한 노드
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  # 재귀 함수

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
visited = [False]*9
dfs(graph, 1, visited)