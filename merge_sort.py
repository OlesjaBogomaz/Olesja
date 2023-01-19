"""
merge_sort принимает на вход массив целых чисел и производит сортировку слиянием
"""

def merge_sort(a):
    if len(a) != 1 and len(a)!=0:
        med = len(a)//2
        l = a[:med]
        l = merge_sort(l)
        r = a[med:]
        r = merge_sort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
                k += 1
            else:
                a[k] = r[j]
                j += 1
                k += 1
        while i < len(l):
            a[k] = l[i]
            k += 1
            i += 1
        while j < len(r):
            a[k] = r[j]
            k += 1
            j += 1
        return a
    else:
        return a
