import time
import tracemalloc
import numpy as np

# Генерация случайного массива данных
np.random.seed(0)
array = np.random.randint(1, 100, size=1000)

# Функции сортировки
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Функция для измерения времени и памяти
def measure_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    tracemalloc.start()
    result = algorithm(arr.copy())
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    time_taken = end_time - start_time
    memory_used = peak - current
    return time_taken, memory_used, type(result)

# Проверка алгоритмов
algorithms = [("Quicksort", quicksort), ("Heapsort", heapsort), ("Merge Sort", merge_sort)]
for name, algorithm in algorithms:
    time_taken, memory_used, data_structure = measure_sorting_algorithm(algorithm, array)
    print(f"{name}: Время выполнения = {time_taken:.6f} секунд, Память = {memory_used / 1024:.2f} КБ, Тип структуры данных = {data_structure}")


print("Quicksort: O(n log n) в среднем, O(n²) в худшем случае")
print("Heapsort: O(n log n) всегда")
print("Merge Sort: O(n log n) всегда")

# Вывод таблицы Big O
print("\nИтоговая таблица Big O для каждого алгоритма:")
print("{:<12} {:<15} {:<15} {:<15}".format(
    "Алгоритм", "Лучший случай", "Средний случай", "Худший случай"
))
print("-" * 60)
print("{:<12} {:<15} {:<15} {:<15}".format(
    "Quicksort", "O(n log n)", "O(n log n)", "O(n²)"
))
print("{:<12} {:<15} {:<15} {:<15}".format(
    "Heapsort", "O(n log n)", "O(n log n)", "O(n log n)"
))
print("{:<12} {:<15} {:<15} {:<15}".format(
    "Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)"
))