def quick_sort(a):
    if len(a) <= 1:
        return a
    stack = [(0, len(a))]
    while stack != []:
        ind1, ind2 = stack.pop()
        e = ind1
        n = ind1+1
        g = e+1
        for _ in range(ind2-ind1-1):
            if a[n] < a[e]:
                y = a[n]
                a[n] = a[g]
                a[g] = a[e]
                a[e] = y
                e += 1
                g += 1
                n += 1
            elif a[e] == a[n]:
                a[g], a[n] = a[n], a[g]
                g += 1
                n += 1
            elif a[n] > a[e]:
                n += 1
        if ind1 != e:
            stack.append((ind1, e))
        if g!=ind2:
            stack.append((g, ind2))
    return a

_ = input()
a = [int(i) for i in input().split()]

import random
random.shuffle(a)

[print(i, end=' ') for i in quick_sort(a)]
