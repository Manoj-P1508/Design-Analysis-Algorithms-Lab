# Warshall's Algorithm (Transitive Closure)
def warshall(n, graph):
    d = []
    for i in range(n):
        d.append(graph[i][:])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = d[i][j] or (d[i][k] and d[k][j])

    print("\nTransitive Closure Matrix:")
    for i in range(n):
        for j in range(n):
            print(d[i][j], end=" ")
        print()

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 or 1):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
warshall(n, graph)