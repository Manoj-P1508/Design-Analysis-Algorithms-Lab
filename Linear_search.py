import time
import matplotlib.pyplot as plt # type: ignore

# Linear Search Function
def linear_search(arr, key):  # sourcery skip: use-next
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Number of experiments
# sourcery skip: for-index-underscore
experiments = int(input("Enter the number how many times you want to Run the linear search: "))

n_values = []
times = []

for _ in range(experiments):
    n = int(input("\nEnter number of elements: "))
    n_values.append(n)

    arr = []
    print("Enter elements:")
    for i in range(n):
        num = int(input())
        arr.append(num)

    key = int(input("Enter element to search: "))

    # Measure time
    start = time.time()
    result = linear_search(arr, key)
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
plt.title("Linear Search: Time vs n")
plt.grid(True)
plt.show()