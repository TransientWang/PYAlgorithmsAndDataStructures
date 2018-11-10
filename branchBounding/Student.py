# -*- coding: UTF-8 -*-
class Student(object):



    def __init__(self):
        self._kk="kk"
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, val):
        self._birth = val

    @property
    def age(self):
        return 2018 - self.birth


    def getSc(self):
        self.ddd = 1
        return self.ddd


    @property
    def score(self):
        print("hello")
        return self._score


    @score.setter
    def score(self, value):
        if value > 100:
            raise AssertionError("大了")
        else:
            self._score = value


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        print(("我被调用"), end=' ')
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            list = []
            for i in range(end):
                if i >= start:
                    list.append(a)
                a, b = b, a + b
            return list

    def __getattr__(self, item):
        if item == "name":
            return "斐波那契数列"
        # raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


    def __str__(self):
        return "obj:斐波那契数列"

if __name__ == '__main__':
    s = Student()
    print((s._kk))
    s._score = 99
    print((s._score))
    s.score = 98
    print((s.score))
    s.birth = 2000
    print((s.age))

    f = Fib()
    for n in f:
        print((n), end=' ')
    print()
    print((f[3]))
    # print(list(range(100))[5:10])
    print((f[:19]))
    print((f.name))
