# Simple Kruskal's Algorithm 

def find(parent, i):
    # Find parent of node
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def kruskal(V, edges):
    # Step 1: Sort edges
    edges.sort(key=lambda x: x[2])

    parent = []
    for i in range(V):
        parent.append(i)

    mst = []   # T = empty
    i = 0      # edge index

    # Step 2: Pick edges until we get V-1 edges
    while len(mst) < V - 1:
        u, v, w = edges[i]
        i += 1

        # Find roots
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If no cycle
        if root_u != root_v:
            mst.append((u, v, w))   # T = T + (u,v)
            parent[root_v] = root_u
        # else ignore (delete edge)

    # Print result
    print("\nEdges in MST:")
    total = 0
    for u, v, w in mst:
        print(u, "--", v, "=", w)
        total += w

    print("Minimum Cost =", total)


# 🔽 Input
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Run
kruskal(V, edges)