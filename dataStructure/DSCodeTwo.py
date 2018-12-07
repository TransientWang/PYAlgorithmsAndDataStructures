# -*- coding: UTF-8 -*-
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(head):
    '''
    赋值随机指针
    :param head:
    :return:
    '''
    if not head:
        return None
    cur = head
    while cur:  # 复制一个新指针在原指针后面
        node = RandomListNode(cur.label)
        node.next = cur.next
        cur.next = node
        cur = node.next
    cur = head
    while cur:  # 复制随机指针
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur = head
    res = head.next
    while cur:  # 将原指针移除
        tmp = cur.next  # node
        cur.next = tmp.next
        if tmp.next:
            tmp.next = tmp.next.next
        cur = cur.next
    return res


if __name__ == '__main__':
    pass
