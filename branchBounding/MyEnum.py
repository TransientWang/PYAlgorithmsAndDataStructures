# -*- coding: UTF-8 -*-

class MyMetaClass(type):

    def __new__(cls, *args, **kwargs):
        # print(cls)
        # print("\n")
        # print(args[1])
        kwargs["add"] = lambda self, value: self.append(value)
        # print("\n")
        # print(kwargs.keys())
        # print("\n")
        # return type( "add",(list,), kwargs)
        return type(args[0],args[1], kwargs)

class MyList(list):
    __metaclass__ = MyMetaClass

if __name__ == '__main__':
        li = MyList()
        li.add(1)
        li.add(2)
        print(li)
        print(li.__class__)
