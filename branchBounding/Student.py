# -*- coding: UTF-8 -*-
class Student(object):

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
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        print("我被调用"),
        self.a,self.b = self.b,self.a+self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        a,b =1,1
        for i in range(item):
            a,b=b,a+b
        return a
if __name__ == '__main__':
    s = Student()
    s._score = 99
    print(s._score)
    s.score=98
    print(s.score)
    s.birth = 2000
    print(s.age)

    f = Fib()
    for n in f:
        print(n),
    print()
    print(f[3])