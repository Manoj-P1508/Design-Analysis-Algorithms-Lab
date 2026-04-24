import time
import matplotlib.pyplot as plt

def partition(a, lb, ub):
    pivot = a[lb]
    start = lb
    end = ub

    while start < end:
        while start <= ub and a[start] <= pivot:
            start += 1

        while a[end] > pivot:
            end -= 1

        if start < end:
            a[start], a[end] = a[end], a[start]

    a[lb], a[end] = a[end], a[lb]
    return end

def quicksort(a, lb, ub):
    if lb < ub:
        loc = partition(a, lb, ub)
        quicksort(a, lb, loc - 1)
        quicksort(a, loc + 1, ub)

k = int(input("Enter number of test cases: "))

n_values = []
times = []

for i in range(k):
    n = int(input("\nEnter number of elements: "))
    a = list(map(int, input("Enter elements: ").split()))

    if len(a) != n:
        print("Error: Enter exactly", n, "elements")
        exit()

    start_time = time.time()
    quicksort(a, 0, n - 1)
    end_time = time.time()

    print("Sorted array:", a)

    n_values.append(n)
    times.append(end_time - start_time)

plt.figure()
plt.plot(n_values, times)
plt.xlabel("Number of elements (n)")
plt.ylabel("Time taken (seconds)")
plt.title("Quick Sort: Time vs n")
plt.grid()
plt.show()