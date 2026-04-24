import random
import time
import matplotlib.pyplot as plt # type: ignore
# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        Min = i
        for j in range(i+1, n):
            if arr[j] < arr[Min]:
                Min = j
        arr[i], arr[Min] = arr[Min], arr[i]
# Different values of n
# sourcery skip: for-index-underscore
sizes = [10, 20, 30, 40, 50]
time_taken = []
for n in sizes:
    arr = [random.randint(1, 100) for i in range(n)]
    start = time.time()
    selection_sort(arr)
    end = time.time()
    time_taken.append(end - start)
# Plot graph
plt.figure()
plt.plot(sizes, time_taken)
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken")
plt.title("Selection Sort Time Complexity")
plt.grid(True)
plt.show()