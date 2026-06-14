import timeit
import random
import matplotlib.pyplot as plt

def bubble_sort(input_list):
    sorted_list = input_list.copy()
    n = len(sorted_list)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True
        if not swapped:
            break
    return sorted_list

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  

random.seed(42)
sizes = [10, 50, 100, 200, 300]  # Разные размеры массивов для тестирования
bubble_times = []
selection_times = []

for size in sizes:   
    unsorted_data = [random.randint(1, 500) for _ in range(size)]
    
    # Замер времени для пузырьковой сортировки
    bubble_time = timeit.timeit(
        lambda: bubble_sort(unsorted_data),
        number=100  # Выполняем 100 раз 
    )
    bubble_times.append(bubble_time)
    
    # Замер времени для сортировки выбором
    selection_time = timeit.timeit(
        lambda: selection_sort(unsorted_data.copy()),  # Используем копию, чтобы не изменять исходный массив
        number=100
    )
    selection_times.append(selection_time)

# Вывод результатов
print("Результаты замеров времени (в секундах, 100 запусков):")
for i, size in enumerate(sizes):
    print(f"Размер {size}: пузырьковая = {bubble_times[i]:.6f}, выбор = {selection_times[i]:.6f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label='Пузырьковая сортировка', marker='o')
plt.plot(sizes, selection_times, label='Сортировка выбором', marker='s')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение производительности алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.show()
