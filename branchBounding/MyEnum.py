# -*- coding: UTF-8 -*-

class MyMetaClass(type):

    def __new__(cls, *args, **kwargs):
        # print(cls)
        # print("\n")
        # print(args[1])
        # kwargs["add"] = lambda self, value: self.append(value)
        # print("\n")
        # print(kwargs.keys())
        return type( "add",(list,), {"add":lambda self, value: self.append(value)})

class MyList(list):
    __metaclass__ = MyMetaClass

if __name__ == '__main__':
        li = MyList()
        li.add(1)
        li.add(2)
        print(li)
