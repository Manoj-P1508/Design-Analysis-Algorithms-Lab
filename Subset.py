# Subset Sum
found=False
def subset_sum(s, target, subset, index):
    global found
    if target == 0:                # If target becomes 0, subset is found
        print(subset)
        found=True
        return
    
    for i in range(index, len(s)): # Traverse remaining elements
        if s[i] <= target:         # Include element only if it does not exceed target
            subset.append(s[i])    # Choose element
            subset_sum(s, target - s[i], subset, i + 1)     # Recur for remaining sum
            subset.pop()                                    # Backtrack

s = list(map(int, input("Enter set elements: ").split()))
d = int(input("Enter target sum: "))
print("Subsets with sum", d, "are:")
subset_sum(s, d, [], 0)
if not found:
    print("NO possible solution")
