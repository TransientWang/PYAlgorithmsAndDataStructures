# -*- coding: UTF-8 -*-
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)
