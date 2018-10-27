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


if __name__ == '__main__':
    s = Student()
    s._score = 99
    print(s._score)
    s.score=98
    print(s.score)
    s.birth = 2000
    print(s.age)
