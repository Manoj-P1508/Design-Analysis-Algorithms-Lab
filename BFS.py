from collections import deque
# Number of vertices
n = int(input("Enter number of vertices: "))
graph = {}
# Taking adjacency list from user
for i in range(n):
    node = input("Enter vertex: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors
# Starting node
start = input("Enter starting vertex: ")
# BFS function
def bfs(graph, start):
    visited = []
    queue = deque()
    visited.append(start)
    queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("BFS Traversal:")
bfs(graph, start)