def compute_sp(s):  ## определим суффикс-префикс функцию
    m = len(s)
    sp = [0] * m
    j = 0
    for i in range(1, m):
        while (j > 0) and (s[i] != s[j]):
            j = sp[j - 1]
        if s[i] == s[j]:
            sp[i] = j + 1
            j += 1
    return sp


def kmp_matcher(pat, text):
    sp = compute_sp(pat)
    k, l = 0, 0
    res = []

    while k < len(text) and l < len(pat):
        if pat[l] == text[k]:  ## если очередная буква текста соответствует - идем дальше
            k += 1
            l += 1
            if l == len(pat):  ## если дошли до конца паттерна - обнулимся и добавим координату в ответ
                l = 0
                res += [k - len(pat)]
                k -= len(pat) - 1
        elif l > 0:  # если непопали - перейдем по суффикс-префикс координате
            l = sp[l - 1]
        else:  # если предыдущим шагом обнулились - идем дальше
            k += 1

    if res == []:
        return -1  ## вывожу минус единицу, если нет вхождений паттерна
    else:
        return res
