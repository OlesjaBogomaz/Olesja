"""

конечный автомат для поиска паттерна в тексте

"""

class StateMachine:
    def __init__(self, pattern):
        self.pattern = pattern
        self.alph = list(set(list(pattern)))
        self.alph.sort()
        s = pattern
        m = len(s)
        sp = [0] * m
        j = 0
        for i in range(1, m):
            while (j > 0) and (s[i] != s[j]):
                j = sp[j - 1]
            if s[i] == s[j]:
                sp[i] = j + 1
                j += 1
        self.st_table = [[0 for i in range(len(self.alph))] for j in range(len(pattern)+1)]  # посчитаем суффикс-префикс функцию
        for j in range(len(self.alph)):
            if pattern[0] == self.alph[j]:
                self.st_table[0][j] = 1
        for i in range(1, len(pattern)):  #  исходя из нее построим таблицу переходов
            for j in range(len(self.alph)):
                if pattern[i] == self.alph[j]:
                    self.st_table[i][j] = i+1
                else:
                    self.st_table[i][j] = self.st_table[sp[i-1]][j]
        for j in range(len(self.alph)):
            self.st_table[len(pattern)][j] = self.st_table[sp[len(pattern) - 1]][j]

    def search(self, text):
        state_arr = [0]
        ind_arr = []
        state = 0
        for i in range(len(text)):
            for j in range(len(self.alph)):
                if self.alph[j] == text[i]:
                    state = self.st_table[state][j]
            if text[i] not in self.alph:
                state = 0
            state_arr += [state]

        for i in range(len(state_arr)):
            if state_arr[i] == len(self.pattern):
                ind_arr += [i-len(self.pattern)]
        print(' '.join([str(i) for i in ind_arr]))