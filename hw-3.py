import random
import time
import tracemalloc
import heapq

# Функция для генерации почти отсортированного массива данных
def generate_nearly_sorted_array(size):
    array = list(range(1, size + 1))
    random.shuffle(array[:50])
    return array

# Функция для генерации большого случайного массива данных
def generate_large_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Функция для генерации случайного массива данных
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Функция для генерации обратно отсортированного массива данных
def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

# Алгоритмы сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapsort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
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

# Тестирование алгоритмов на различных массивах данных
def test_sorting_algorithms(array, array_name):
    print(f"\nТестирование на {array_name}")

    for algorithm in [("Quick Sort", quick_sort), ("Heapsort", heapsort), ("Merge Sort", merge_sort)]:
        name, func = algorithm
        start_time = time.time()
        tracemalloc.start()
        sorted_array = func(array.copy())
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        print(f"{name}")
        print("Время работы:", end_time - start_time)
        print("Объем затрачиваемой оперативной памяти:", peak / 10**6, "MB")

# Генерация массивов данных
nearly_sorted_array = generate_nearly_sorted_array(1000)
large_random_array = generate_large_random_array(10000)
random_array = generate_random_array(1000)
reverse_sorted_array = generate_reverse_sorted_array(1000)

# Тестирование
test_sorting_algorithms(nearly_sorted_array, "почти отсортированном массиве")
test_sorting_algorithms(large_random_array, "большом случайном массиве")
test_sorting_algorithms(random_array, "случайном массиве (размер 1000)")
test_sorting_algorithms(reverse_sorted_array, "обратно отсортированном массиве")
