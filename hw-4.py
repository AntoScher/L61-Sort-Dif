import random
import time
import tracemalloc
import heapq

# Функция для генерации массива данных, где большинство элементов одинаковы, но есть несколько случайных чисел
def generate_special_array(size, unique_elements):
    array = [42] * (size - unique_elements)
    array += [random.randint(1, 1000000) for _ in range(unique_elements)]
    random.shuffle(array)
    return array

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

# Тестирование алгоритмов на специальном массиве данных
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

# Генерация специального массива данных
special_array = generate_special_array(100000, 50)

# Тестирование
test_sorting_algorithms(special_array, "специальном массиве данных")
