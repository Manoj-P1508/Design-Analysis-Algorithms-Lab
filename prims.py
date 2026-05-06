# Simple Prim's Algorithm

def prim(n, cost):
    visited = [0] * n   # visited array

    # Step 1: start from vertex 0
    visited[0] = 1
    edges = 0
    total_cost = 0

    print("\nEdges in MST:")

    # Step 2: repeat until n-1 edges
    while edges < n - 1:
        min_val = 999
        u = -1
        v = -1

        # find minimum edge between visited and unvisited
        for i in range(n):
            if visited[i] == 1:
                for j in range(n):
                    if visited[j] == 0 and cost[i][j] < min_val:
                        min_val = cost[i][j]
                        u = i
                        v = j

        # add edge to MST
        print(u, "--", v, "=", min_val)
        total_cost += min_val
        visited[v] = 1
        edges += 1

    print("Minimum Cost =", total_cost)


# 🔽 Input
n = int(input("Enter number of vertices: "))

print("Enter cost adjacency matrix:")
cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

# Replace 0 with large value (no edge)
for i in range(n):
    for j in range(n):
        if cost[i][j] == 0:
            cost[i][j] = 999

# Run Prim's
prim(n, cost)