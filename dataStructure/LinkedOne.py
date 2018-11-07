# -*- coding: UTF-8 -*-

'''
删除链表中的节点
由于只有下一个节点 不能获取到上一节点
解决办法是 将下一节点的值 赋值给当前被删除节点，然后删除下一节点
'''


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


'''
删除链表的倒数第N个节点
'''
def removeNthFromEnd(self, head, n):
    pass

    if __name__ == '__main__':
        pass
