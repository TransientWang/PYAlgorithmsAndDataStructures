# -*- coding: UTF-8 -*-
import os


class MyFile(object):
    def dealFile(self, path: str, oldPrefix, newPrefix):
        if path.endswith(oldPrefix):
            print(path[:path.rindex(".")] + "." + newPrefix)
            print(os.rename(path, path[:path.rindex(".")] + "." + newPrefix))

    def renameFile(self, path: str, oldPrefix="jsp", newPrefix="html"):
        """
        递归修改后缀
        :param path:
        :param oldPrefix:
        :param newPrefix:
        :return:
        """
        if os.path.isfile(path):
            self.dealFile(path, oldPrefix, newPrefix)
        else:
            dirs = os.listdir(path)
            for name in dirs:
                self.renameFile(path + "\\" + name, oldPrefix, newPrefix)
