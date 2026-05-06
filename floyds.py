# Floyd-Warshall using d[i][j] = min(d[i][j], d[i][k] + d[k][j])
INF = 99999
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Initialize adjacency matrix
d = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            row.append(INF)
    d.append(row)

# Taking edges input
print("Enter edges (u v w):")
for _ in range(e):
    u, v, w = map(int, input().split())
    d[u][v] = w   # directed graph

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

# Output
print("\nShortest distance matrix:")
for i in range(n):
    for j in range(n):
        if d[i][j] == INF:
            print("INF", end="\t")
        else:
            print(d[i][j], end="\t")
    print()