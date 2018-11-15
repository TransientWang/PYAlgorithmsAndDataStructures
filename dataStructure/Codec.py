# -*- coding: UTF-8 -*-
from dataStructure import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        res = []
        queue = []
        queue.append(root)

        while len(queue) != 0:
            tmp = queue.pop(0)
            if not tmp is None:
                res.append(tmp.val)

                if tmp.left is None:
                    queue.append(None)
                else:
                    queue.append(tmp.left)
                    # res.append(tmp.left.val)
                if tmp.right is None:
                    queue.append(None)
                else:
                    queue.append(tmp.right)
                    # res.append(tmp.right.val)

            else:
                res.append(None)
        while res[-1] is None:
            res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        stack = []
        root = TreeNode.TreeNode(data.pop(0))
        stack.append(root)
        while len(data) != 0:
            tmp = stack.pop(0)
            if len(data) > 0:

                if len(data)>0 and data[0] is None:
                    data.pop(0)
                elif len(data)>0 :
                    leftNode = TreeNode.TreeNode(data.pop(0))
                    tmp.left = leftNode
                    stack.append(leftNode)
                if len(data)>0 and data[0] is None:
                    data.pop(0)
                elif len(data)>0:
                    rightNode = TreeNode.TreeNode(data.pop(0))
                    tmp.right = rightNode
                    stack.append(rightNode)

        return root


if __name__ == '__main__':
    root = TreeNode.TreeNode(1)
    root.left = TreeNode.TreeNode(2)
    # root.right = TreeNode.TreeNode(3)
    # root.right.left = TreeNode.TreeNode(4)
    # root.right.right = TreeNode.TreeNode(5)
    c = Codec()
    print(c.serialize(root))
    k = c.deserialize([1, 2])
    print(k)
