# -*- coding: UTF-8 -*-
class RestChain(object):
    def __init__(self, path="https:/"):
        self._path = path
        self.name = "测试类"

    def __str__(self):
        return self._path

    def users(self, user):
        return RestChain("users/%s" % user)

    def __getattr__(self, item):
        return RestChain("%s/%s" % (self._path, item))

    def __call__(self, *args, **kwargs):
        return "这个类是一个rest风格的调用：%s" % self.name

if __name__ == '__main__':
    print(RestChain().users("wfy").profile.reposiory)

    rest = RestChain()
    print(rest())