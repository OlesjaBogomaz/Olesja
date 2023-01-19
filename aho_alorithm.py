import queue
class Node:
    def __init__(self, parent=None):
        self.obj = None
        self.link = dict()
        self.parent = parent
        self.f = None
        self.o = None
        self.go = dict()


class AhoEasy:
    def __init__(self):
        self.prehead = Node()
        self.head = Node()
        alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
        for i in alph:
            self.prehead.link[i] = self.head
        self.patterns = []

    def add_pattern(self, pattern):  # строим бор
        cur = self.head
        for i in range(len(pattern)):
            if pattern[i] not in cur.link.keys():
                cur.link[pattern[i]] = Node(parent=cur)
            cur = cur.link[pattern[i]]
            if i == len(pattern)-1:
                cur.obj = pattern
        self.patterns += [pattern]

    def f_calculation(self):  # проставляем суффиксные ссылки, проходя по бору в ширину
        cur = self.head
        cur.f = self.prehead
        q = queue.SimpleQueue()
        for key in  cur.link.keys():
            q.put((key, cur.link[key]))
        while q.qsize() != 0:
            cur = q.get()
            i = cur[0]
            cur = cur[1]
            f_cal = cur.parent
            while cur.f is None:
                f_cal = f_cal.f
                if i in f_cal.link.keys():
                    f_cal = f_cal.link[i]
                    cur.f = f_cal
            for key in cur.link.keys():
                q.put((key, cur.link[key]))

    def o_calculation(self):  # проставляем хорошие суффиксные ссылки, проходясь в глубину
        self.head.o = self.head
        for pattern in self.patterns:
            cur = self.head
            for i in pattern:
                cur = cur.link[i]
                o_cal = cur.f
                while cur.o is None:
                    if o_cal.obj is not None or o_cal.parent is None:
                        cur.o = o_cal
                    else:
                        o_cal = o_cal.f

    def getlink(self, v, c):  # собственно функция перехода
        if c not in v.go.keys():
            if c in v.link.keys(): # если из вершины есть такое ребро, то это и будет переходом
                v.go[c] = v.link[c]
            elif v.parent is None:  # если это корень, то остаемся в нем и ждем, когда придет подходящий символ
                v.go[c] = v
            else:
               v.go[c] = self.getlink(v.f, c)  # иначе перейдем по сууфиксной ссылке (и на месте сделаем ее), а потом попробуем перейти по тому же символу
        return v.go[c]  # если ранее уже просчитывали такой переход - выведи

    def search(self, text):
        self.f_calculation()
        self.o_calculation()
        cur = self.head
        to_return = []
        for i in range(len(text)):
            c = text[i]
            cur = self.getlink(cur, c)  # применим функцию перехода
            if cur.obj is not None:
                to_return += [(i - len(cur.obj) + 1, cur.obj)]
            o_link = cur.o
            while o_link.parent is not None:  # из полученного состояния пройдемся по хорошим суфф ссылкам, чтоб ничего не упустить
                to_return += [(i - len(o_link.obj) + 1, o_link.obj)]
                o_link = o_link.o
        return to_return