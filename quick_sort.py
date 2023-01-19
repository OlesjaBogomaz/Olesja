"""
quick_sort принимает на вход массив целых чисел и производит быструю сортировку
"""

def quick_sort(a):
    import random

    random.shuffle(a)  # перемешиваем, чтобы в случае предварительной сортировки массива не получить квадратичное время
    pivot = 0
    if len(a) > 0:
        pointer = len(a) - 1
    else:
        return a
    while pivot != pointer:
        while a[pivot] < a[pointer]:
            pointer -= 1
        a[pivot], a[pointer] = a[pointer], a[pivot]
        pivot, pointer = pointer, pivot

        if pointer != pivot and a[pivot] == a[pointer]:
            pointer += 1
        while a[pivot] > a[pointer]:
            pointer += 1
        a[pivot], a[pointer] = a[pointer], a[pivot]
        pivot, pointer = pointer, pivot
    return quick_sort(a[:pivot]) + [a[pivot]] + quick_sort(a[pivot + 1:])
