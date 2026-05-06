def optimal_bst(p, n):
    C = [[0]*(n+2) for _ in range(n+2)]
    R = [[0]*(n+2) for _ in range(n+2)]

    for i in range(1, n+1):
        C[i][i] = p[i] 
        R[i][i] = i           
        C[i][i-1] = 0         

    C[n+1][n] = 0            

    for length in range(2, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1

            C[i][j] = float('inf')
            total = sum(p[i:j+1])

            for k in range(i, j+1):
                cost = C[i][k-1] + C[k+1][j] + total

                if cost < C[i][j]:
                    C[i][j] = cost
                    R[i][j] = k

    return C, R
n = int(input("Enter number of keys: "))
print("Enter probabilities:")
probs = list(map(float, input().split()))
p = [0] + probs
C, R = optimal_bst(p, n)

print("\nCost Table:")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(C[i][j], end=" ")
    print()

print("\nRoot Table:")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(R[i][j], end=" ")
    print()

print("\nMinimum Cost:", C[1][n])