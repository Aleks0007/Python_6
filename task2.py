"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
"""

def find_indexes_in_range(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

# пример использования
my_list = [3, 5, 1, 2, 7, 9, 10]
min_val = 2
max_val = 8
result_indexes = find_indexes_in_range(my_list, min_val, max_val)
print(result_indexes)