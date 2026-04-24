import time
import matplotlib.pyplot as plt

# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Number of experiments
experiments = int(input("Enter number of different n values: "))

n_values = []
times = []

for _ in range(experiments):

    n = int(input("\nEnter number of elements: "))
    n_values.append(n)

    arr = []
    print("Enter elements (sorted or unsorted):")
    for _ in range(n):
        num = int(input())
        arr.append(num)

    arr.sort()   # Binary search requires sorted list

    key = int(input("Enter element to search: "))

    start = time.time()
    result = binary_search(arr, key)
    end = time.time()

    times.append(end - start)

    if result != -1:
        print("Element found at position:", result + 1)
    else:
        print("Element not found")

    print("Time taken:", end - start, "seconds")


# Plot Graph
plt.figure()
plt.plot(n_values,times,'o-')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Binary Search: Time vs n")
plt.grid(True)
plt.show()