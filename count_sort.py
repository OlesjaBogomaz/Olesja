"""
Реализуем сортировку подсчетом

"""

def count_sort(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    count = [0 for i in range(max_arr - min_arr + 1)]
    for i in arr:
        count[i - min_arr] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    new_arr = [None for i in range(len(arr))]
    arr = arr[::-1]
    for i in range(len(arr)):
        ind = count[arr[i] - min_arr] - 1
        while new_arr[ind] != None:
            ind = ind - 1
        new_arr[ind] = arr[i]
    return new_arr
