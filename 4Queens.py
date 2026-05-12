# N Queen Problem using Backtracking
n = 4
x = [0] * (n + 1)   # Stores queen positions
# Function to check whether queen can be placed safely
def place(k, i):
    for j in range(1, k):
        # Check same column
        if x[j] == i:
            return False
        # Check diagonal
        if abs(x[j] - i) == abs(j - k):
            return False
    return True
# Function to solve N Queens
def NQueens(k, n):
    for i in range(1, n + 1):
        if place(k, i):
            # Place queen
            x[k] = i
            # If all queens are placed
            if k == n:
                print("Solution:")
                for row in range(1, n + 1):
                    for col in range(1, n + 1):
                        if x[row] == col:
                            print("Q", end=" ")
                        else:
                            print(".", end=" ")
                    print()
                print()
            else:
                # Place queen in next row
                NQueens(k + 1, n)
NQueens(1, n)