def bubble_sort(input_list):
   
    # Создаем копию списка, чтобы не изменять оригинал
    sorted_list = input_list.copy()
    n = len(sorted_list)

    for i in range(n - 1):
        swapped = False  # Флаг для отслеживания обменов

        # Проходим по неотсортированной части списка
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Меняем элементы местами
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True

        # Если обменов не было, список отсортирован
        if not swapped:
            break

    return sorted_list


my_numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(my_numbers)
print("Исходный список:", my_numbers)
print("Отсортированный список:", sorted_numbers)